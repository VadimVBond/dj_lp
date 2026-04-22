from django.urls import path, include
from django.http import HttpResponse
from django_distill import distill_path
from core.views import index

def get_langs():
    for lang in ['en', 'ru', 'uk']:
        yield {'lang': lang}

def get_root():
    return None

def root_redirect(request):
    return HttpResponse(
        '<html><head><meta http-equiv="refresh" content="0; url=en/"></head></html>'
    )

urlpatterns = [
    distill_path(
        '',
        root_redirect,
        name='root_redirect',
        distill_func=get_root,
        distill_file='index.html'
    ),
    distill_path(
        '<str:lang>/',
        index,
        name='index',
        distill_func=get_langs
    ),
]
