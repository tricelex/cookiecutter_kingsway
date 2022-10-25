from config.env import env

# https://docs.celeryproject.org/en/stable/userguide/configuration.html

# ######### RABBITMQ CONFIGURATION ###########
RABBITMQ_HOST = 'rabbitmq'
RABBITMQ_PORT = 5672
RABBITMQ_VHOST = 'my_vhost'
RABBITMQ_USER = 'rabbitmq'
RABBITMQ_PASSWORD = 'rabbitmq'
RABBITMQ_MANAGEMENT_API_PORT = 15672
RABBITMQ_MANAGEMENT_API_USER = 'rabbitmq'
RABBITMQ_MANAGEMENT_API_PASSWORD = 'rabbitmq'
RABBITMQ_MANAGEMENT_API_BASE_URL = f'http://{RABBITMQ_HOST}:{RABBITMQ_MANAGEMENT_API_PORT}/api'

# ######### CELERY CONFIGURATION ###########
BROKER_URL = f'amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{RABBITMQ_VHOST}'
BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': 3600,
    'fanout_prefix': True,
    'fanout_patterns': True,
}  # 1 hour
DEVICE_INFO_QUEUE = 'celery'  # This is the default queue for Celery
DAILY_TASKS_QUEUE = 'celery'  # This is the default queue for Celery
LOW_PRIORITY_TASKS_QUEUE = 'celery'  # This is the default queue for Celery
LOAN_SCORING_DISBURSEMENT_QUEUE = 'celery'  # This is the default queue for Celery
REPAYMENT_TASKS_QUEUE = 'celery'  # This is the default queue for Celery
LOAN_RECONCILIATION_TASKS_QUEUE = 'celery'
CELERY_ENABLE_UTC = False


CELERY_TIMEZONE = 'UTC'
CELERY_TASK_MAX_RETRIES = 3

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = BROKER_URL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_backend
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-always-eager
CELERY_TASK_ALWAYS_EAGER = False
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True