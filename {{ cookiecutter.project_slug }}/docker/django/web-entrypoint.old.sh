#!/usr/bin/env bash

until cd config
do
    echo "Waiting for django volume..."
done

until poetry run python manage.py migrate --settings=quickcheckbackend.settings.dev
do
    echo "Waiting for postgres ready..."
done

poetry run python manage.py collectstatic --clear --noinput --settings=quickcheckbackend.settings.dev
poetry run python manage.py loaddata accounts/fixtures/dashboard_users_dev.json --settings=quickcheckbackend.settings.dev
poetry run python manage.py runserver 0.0.0.0:8000 --settings=quickcheckbackend.settings.dev
