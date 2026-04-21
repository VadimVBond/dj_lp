"""
Django settings for landing_project project.
"""
import os

# Default to dev settings if not specified
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.dev'
