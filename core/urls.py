from django_distill import distill_path
from .views import index

app_name = "core"

urlpatterns = [
    distill_path("en/", index, name="index_en"),
    distill_path("ru/", index, name="index_ru"),
    distill_path("uk/", index, name="index_uk"),
]
