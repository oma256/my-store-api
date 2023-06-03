FROM python:3.9
MAINTAINER  Dulatov Omurbek <oma.dulatov@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app
COPY . .

RUN pip install -r requirements/prod.txt

EXPOSE 8000
