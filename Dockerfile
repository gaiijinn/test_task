FROM python:3.11-alpine

COPY requirements.txt /temp/requirements.txt
COPY test_project /test_project

WORKDIR test_project
EXPOSE 800

RUN pip install --upgrade pip && \
    pip install -r /temp/requirements.txt

RUN adduser --disabled-password gaijin
USER gaijin