from django.urls import path
from .views import *

urlpatterns = [
    path('', mypage, name="mypage"),
    path('edit/', edit, name="edit"),
    path('comments/', comments, name="comments"),
]