from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:detail_id>', views.detail, name = "detail"),
    path('<int:detail_id>/delete', views.delete, name = "delete"),
    path('<int:detail_id>/edit', views.edit, name = "edit"),
    
]