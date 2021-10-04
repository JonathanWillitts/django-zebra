from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edc/", views.edc, name="edc"),
    path("sample/", views.sample, name="sample"),
]
