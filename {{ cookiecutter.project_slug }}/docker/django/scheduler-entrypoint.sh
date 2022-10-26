#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail


rm -f /celerybeat/*.pid

celery -A {{ cookiecutter.project_slug }}.tasks.celery beat -l INFO --pidfile= --schedule=/celerybeat/celerybeat-schedule
 