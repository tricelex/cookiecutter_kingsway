#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

watchfiles celery.__main__.main --args '-A {{ cookiecutter.project_slug }}.tasks.celery worker -l INFO'