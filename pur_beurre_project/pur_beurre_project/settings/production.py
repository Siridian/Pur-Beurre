from . import *

import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentrt_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(
    level = logging.INFO,
    event_level = logging.ERROR
)

sentry_sdk.init(
    dsn="https://c24feb968049494ca72c4ba70e5c13e4@sentry.io/1773298",
    integrations=[DjangoIntegration(), sentry_logging]
)

SECRET_KEY = 'Y,."IT1.`-\rOB\x0c~irF%+`rP6'
DEBUG = True
ALLOWED_HOSTS = ['134.209.183.242']

DATABASES = {
            'default': {
                     'ENGINE': 'django.db.backends.postgresql',
                     'NAME': 'pur_beurre_db',
                     'USER': 'vsorba', 
                     'PASSWORD': 'Retenir00',
                     'HOST': '',
                     'PORT': '5432',
            }
}
            
