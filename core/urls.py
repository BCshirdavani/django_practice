from django.urls import path

from . import views

urlpatterns = [
    path("images/", views.image_list, name="image-list"),
    path("images/<int:image_id>/", views.image_detail, name="image-detail"),
]