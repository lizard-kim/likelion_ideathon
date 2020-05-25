from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mypage, name="mypage"),
    path('mypageedit/', mypageedit, name="mypageedit"),
    path('comments/', comments, name="comments"),
]