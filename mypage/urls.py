from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mypage, name="mypage"),
    path('comments/', comments, name="comments"),
]