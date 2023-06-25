#!/bin/bash

echo "===== Running migrate"
python manage.py migrate

echo "===== Running collectstatic"
python manage.py collectstatic --noinput

echo "===== Running compilemessages"
python manage.py compilemessages

echo "===== Running createsuperuser"
python manage.py createsuperuser --noinput --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL"

echo "Provisioning done"
