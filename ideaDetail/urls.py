from django.urls import path
<<<<<<< HEAD
from .views import detail

urlpatterns = [
    path('', detail, name="detail")
=======
from . import views

urlpatterns = [
    path('<int:detail_id>', views.detail, name = "detail"),
    path('<int:detail_id>/delete', views.delete, name = "delete"),
>>>>>>> idea & detail 연결 및 수정
]