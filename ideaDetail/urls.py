from django.urls import path
from . import views

urlpatterns = [
    path('<int:detail_id>', views.detail, name = "detail"),
    path('<int:detail_id>/delete', views.delete, name = "delete"),
]