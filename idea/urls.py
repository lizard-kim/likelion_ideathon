from django.urls import path, include
from .views import idea

urlpatterns = [
    path('', idea, name="idea"),
    path('detail/', include('ideaDetail.urls')),
]