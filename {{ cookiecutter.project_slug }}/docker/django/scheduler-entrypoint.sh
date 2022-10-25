#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

until cd config
do
    echo "Waiting for volume..."
done

rm -f /celerybeat/*.pid
exec "$@"

celery -A {{ cookiecutter.project_slug }}.tasks.celery beat -l INFO --pidfile=/celerybeat/celerybeat.pid --schedule=/celerybeat/celerybeat-schedule
 