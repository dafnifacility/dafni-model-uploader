import os
import sys
import requests
import argparse
from pathlib import Path
from dafni_cli.login import login
from dafni_cli.nims import (
    validate_model_definition,
    get_model_upload_urls,
    upload_file_to_minio,
    ingest_model,
    NIMSError,
)
from requests.exceptions import ConnectionError

args = sys.argv[1:]
definition_path = Path(args[0])
image_path = Path(args[1])
username = args[2]
password = args[3]
version_message = args[4]
parent_model = args[5] if len(args) > 5 else None

print("Logging in to DAFNI")
jwt = login(username, password)

if jwt is None:
    sys.exit(1)

try:
    print("Validating Model definition")
    valid, errors = validate_model_definition(jwt, definition_path)
    if not valid:
        print("Definition validation failed with the following errors:", errors)
        sys.exit(1)

    print("Get URLs for upload")
    upload_id, urls = get_model_upload_urls(jwt)
    definition_url = urls["definition"]
    image_url = urls["image"]

    print("Upload Model definition")
    upload_file_to_minio(jwt, definition_url, definition_path)
    print("Upload image")
    upload_file_to_minio(jwt, image_url, image_path)

    print("Start Model ingest")
    ingest_model(jwt, upload_id, version_message, parent_model)

except NIMSError as e:
    print(e.message)
    sys.exit(1)
except ConnectionError as e:
    print(f"Exception thrown during previous request: {e}")
    sys.exit(1)
