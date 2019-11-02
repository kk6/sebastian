FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY pyproject.toml poetry.lock /code/
RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev \
  && pip install poetry \
  && poetry config settings.virtualenvs.create false \
  && poetry install

COPY . /code/
