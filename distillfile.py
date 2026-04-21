"""
Django Distill configuration for static site export.
"""
from django.conf import settings


def get_languages():
    """Return list of language codes for distill."""
    return [lang[0] for lang in settings.LANGUAGES]


def distill_index(language):
    """Return kwargs for index page."""
    return {'language': language}


# Distill configuration
DISTILL_PAGES = [
    {
        'name': 'index',
        'distill_func': get_languages,
        'distill_file': '{language}/index.html',
        'view_name': 'core:index',
        'kwargs_function': distill_index,
    },
]
