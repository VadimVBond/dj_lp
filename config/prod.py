from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

# GitHub Pages subpath (repository name)
FORCE_SCRIPT_NAME = "/dj_lp/"
STATIC_URL = f"{FORCE_SCRIPT_NAME}static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
