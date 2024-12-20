import sys
from pathlib import Path

from dafni_cli.api.session import DAFNISession
from dafni_cli.models.upload import upload_model


args = sys.argv[1:]
definition_path = Path(args[0])
image_path = Path(args[1])
username = args[2]
password = args[3]
version_message = args[4]
parent_model = args[5] if len(args) > 5 else None

print("Logging in to DAFNI")
session = DAFNISession().login(username, password)

if session is None:
    sys.exit(1)

try:
    upload_model(session, definition_path, image_path, version_message, parent_model)
except:
    pass
finally:
    session.logout()
