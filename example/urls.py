# example/urls.py
from django.urls import path, re_path

from example.views import index


urlpatterns = [
    re_path('.*', index),
]
