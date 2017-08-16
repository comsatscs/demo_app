#!/usr/bin/env bash

cd ../ && python manage.py

gunicorn --reload  --log-level info  --workers=3 --timeout 60 --bind 0.0.0.0:8081 manage:app