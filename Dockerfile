FROM python:latest

WORKDIR /workShip

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=11

COPY . .
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev && \
    pip install --no-cache-dir -r requirements.txt