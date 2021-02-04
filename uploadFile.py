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
    start_model_ingest,
    start_model_version_ingest,
)

args = sys.argv[1:]
definition_path = Path(args[0])
image_path = Path(args[1])
username = args[2]
password = args[3]
version_message = args[4]
parent_model = args[5] if len(args) > 5 else None
print(definition_path, image_path, username, password, version_message, parent_model)

print("Logging in to DAFNI")
jwt = login(username, password)
print(jwt)

print("Validate Model definition")
valid, errors = validate_model_definition(jwt, definition_path)
if not valid:
    print("Definition validation failed with the following errors:", errors)
    exit

print("Get Urls")
upload_id, urls = get_model_upload_urls(jwt)
definition_url = urls["definition"]
image_url = urls["image"]

print("Upload Model definition")
upload_file_to_minio(jwt, definition_url, definition_path)
print("Upload image")
upload_file_to_minio(jwt, image_url, image_path)

print("Start Model ingest")
if parent_model == None:
    start_model_ingest(jwt, upload_id, version_message)
else:
    start_model_version_ingest(jwt, parent_model, upload_id, version_message)
