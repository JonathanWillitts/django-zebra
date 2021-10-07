from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edc/", views.edc, name="edc"),
    path("print/<str:label_type>/concise", views.print_concise, name="print_concise"),
    path("print/<str:label_type>/verbose", views.print_verbose, name="print_verbose"),
    path("sample/", views.sample, name="sample"),
]
