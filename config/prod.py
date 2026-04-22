from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

# Static files settings are now handled via environment variables in base.py
STATIC_ROOT = BASE_DIR / "staticfiles"
