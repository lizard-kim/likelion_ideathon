from django.urls import path, include
from .views import *

urlpatterns = [
    path('', mypage, name="mypage"),
    path('comments/', comments, name="comments"),
    path('mypage_edit/', mypage_edit, name="mypage_edit"),
    path('detail/', include('ideaDetail.urls')),
    path('image_edit', image_edit, name = "image_edit"),
]