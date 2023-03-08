#!/bin/sh
FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
  # uwsgi dependencies
  && apt-get install -y gcc \
  # For requirements installed by pip via Gitlab
  && apt-get install -y git
RUN pip install uwsgi psycopg2-binary cython

RUN mkdir /code
COPY main_service/ /code/
COPY requirements.txt /code/
COPY entrypoint.sh /code/
WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt

RUN bash entrypoint.sh
EXPOSE 41666
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:41666" ]