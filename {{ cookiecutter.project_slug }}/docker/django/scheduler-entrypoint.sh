#!/usr/bin/env bash

until cd src
do
    echo "Waiting for volume..."
done

rm -f /celerybeat/*.pid
exec "$@"

C_FORCE_ROOT=true DJANGO_SETTINGS_MODULE="config.django.base" poetry run celery beat -A quickcheckbackend -l debug --pidfile=/celerybeat/celerybeat.pid --schedule=/celerybeat/celerybeat-schedule
