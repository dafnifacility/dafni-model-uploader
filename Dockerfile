FROM python:3.9

ADD requirements.txt requirements.txt
ADD uploadFile.py uploadFile.py
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3", "uploadFile.py" ]