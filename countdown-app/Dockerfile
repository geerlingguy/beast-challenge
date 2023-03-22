# syntax=docker/dockerfile:1.4
FROM python:3-alpine

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DATABASE_PATH=/var/beast/countdown.sqlite

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Install SQLite
RUN apk update && apk upgrade
RUN apk add --no-cache sqlite

COPY . /app

# Initialize the database.
RUN mkdir /var/beast
RUN python3 init_db.py

ENTRYPOINT ["flask"]
CMD ["run"]
