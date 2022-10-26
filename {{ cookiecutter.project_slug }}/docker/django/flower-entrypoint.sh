#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

celery \
    -A {{ cookiecutter.project_slug }}.tasks.celery \
    -b "${CELERY_BROKER_URL}" \
    flower \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
