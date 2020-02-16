#!/bin/sh
FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
  # uwsgi dependencies
  && apt-get install -y gcc \
  # For requirements installed by pip via Gitlab
  && apt-get install -y git
RUN pip install uwsgi psycopg2-binary cython
RUN pip install numpy
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY . /code/