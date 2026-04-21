from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

STATIC_URL = "/static/"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
