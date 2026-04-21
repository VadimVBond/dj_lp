from django_distill import distill_path
from .views import index

app_name = "core"


def get_index_urls():
    return ["en", "ru", "uk"]


urlpatterns = [
    distill_path("<lang>/", index, name="index", distill_func=get_index_urls),
]
