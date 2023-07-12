#!/bin/sh
FROM python:3.11-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
  # uwsgi dependencies
  && apt-get install -y gcc \
  # For requirements installed by pip via Gitlab
  && apt-get install -y git \
  && apt-get install -y curl
RUN pip install uwsgi psycopg2-binary cython

RUN mkdir /code
COPY requirements.txt /code/
COPY entrypoint.dev.sh /
WORKDIR /code
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["/bin/bash", "entrypoint.dev.sh"]