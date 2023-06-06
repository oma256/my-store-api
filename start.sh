#!/usr/bin/env bash

python ./manage.py migrate --noinput
python runserver 0.0.0.0:8000
