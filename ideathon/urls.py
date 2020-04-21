from django.contrib import admin
from django.urls import path, include
import main.urls, about.urls, idea.urls, ideaDetail.urls, mypage.urls, signIn.urls, submit.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about/', include('about.urls')),
    path('idea/', include('idea.urls')),
    path('detail/', include('ideaDetail.urls')),
    path('mypage/', include('mypage.urls')),
    path('signin/', include('signIn.urls')),
    path('submit/', include('submit.urls')),
]
