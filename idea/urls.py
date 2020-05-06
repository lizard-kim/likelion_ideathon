<<<<<<< HEAD
from django.urls import path
from .views import idea

urlpatterns = [
    path('', idea, name="idea")
=======
from django.urls import path, include
from .views import idea

urlpatterns = [
    path('', idea, name="idea"),
    path('detail/', include('ideaDetail.urls')),
>>>>>>> idea & detail 연결 및 수정
]