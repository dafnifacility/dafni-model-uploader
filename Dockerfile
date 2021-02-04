FROM python:3.9

COPY requirements.txt /requirements.txt
COPY uploadModel.py /uploadModel.py
RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3", "/uploadModel.py" ]