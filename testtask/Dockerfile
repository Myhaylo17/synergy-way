FROM python:3.11-slim

WORKDIR /code

# Ставимо залежності для mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
