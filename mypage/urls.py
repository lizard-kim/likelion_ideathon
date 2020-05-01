from django.urls import path
from .views import mypage, edit

urlpatterns = [
    path('', mypage, name="mypage"),
    path('edit/', edit, name="edit"),
]