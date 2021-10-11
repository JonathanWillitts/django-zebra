from django.urls import path

from . import views

urlpatterns = [
    path("create/<int:number_of_slots>", views.create_slots, name="create_slots"),
]
