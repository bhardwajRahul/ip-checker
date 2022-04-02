FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /ip-checker
COPY src /ip-checker
WORKDIR /ip-checker

CMD ["python", "run.py"]
