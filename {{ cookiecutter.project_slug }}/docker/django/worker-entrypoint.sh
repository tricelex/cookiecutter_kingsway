#!/usr/bin/env bash

until cd src
do
    echo "Waiting for volume..."
done

C_FORCE_ROOT=true DJANGO_SETTINGS_MODULE="config.django.base" poetry run celery worker -A quickcheckbackend -l debug
