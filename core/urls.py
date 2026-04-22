from django_distill import distill_path
from .views import index
from .distill import get_index_urls

app_name = "core"

urlpatterns = [
    distill_path(
        "",
        index,
        name="index",
        distill_func=get_index_urls
    ),
]
