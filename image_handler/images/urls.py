from django.conf.urls import url, include
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^images/(<id>)?', views.Images.as_view(), name="image_handler"),
]