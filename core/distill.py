from django.conf import settings
from django.utils import translation


def get_index_urls():
    for lang_code, _ in settings.LANGUAGES:
        translation.activate(lang_code)
        yield None
