"""
Django production settings for static site export.
"""
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# For GitHub Pages deployment, use relative URLs
FORCE_SCRIPT_NAME = None
STATIC_URL = 'static/'

# Distill settings for production
DISTILL_OUTPUT_DIR = BASE_DIR / 'dist'
DISTILL_BASE_URL = '/'
