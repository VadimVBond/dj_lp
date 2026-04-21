from django.urls import path
from django.utils.translation import gettext_lazy as _
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
]
