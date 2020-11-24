FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /ip-checker
COPY ./src /ip-checker
WORKDIR /ip-checker

CMD ["python", "run.py"]
