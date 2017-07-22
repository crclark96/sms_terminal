# Dockerfile
# 21 July 2017
# Collin Clark
# SMS Terminal

FROM python:2

MAINTAINER Collin Clark <crclark96@gmail.com>

WORKDIR /usr/src

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY *.py ./

ENV FLASK_APP main.py

CMD ["flask", "run", "--host=0.0.0.0"]