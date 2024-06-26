#!/bin/sh

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --no-input
python manage.py fill_db
gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000