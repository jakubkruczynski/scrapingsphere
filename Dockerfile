FROM --platform=linux/amd64 python:3.10.7-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
