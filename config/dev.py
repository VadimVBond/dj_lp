from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# STATIC_URL is now inherited from base.py

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
