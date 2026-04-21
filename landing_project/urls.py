from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.http import HttpResponse
from django_distill import distill_path


def get_root():
    return None


def root_static_redirect(request):
    return HttpResponse(
        '<html><head><meta http-equiv="refresh" content="0; url=en/"></head></html>'
    )


urlpatterns = [
    distill_path(
        "",
        root_static_redirect,
        name="root_redirect",
        distill_func=get_root,
        distill_file="index.html"
    ),
]

urlpatterns += i18n_patterns(
    path("", include("core.urls")),
)
