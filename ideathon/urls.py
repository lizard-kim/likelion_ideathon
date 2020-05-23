from django.contrib import admin
from django.urls import path, include
import main.urls, about.urls, idea.urls, ideaDetail.urls, mypage.urls, accounts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about/', include('about.urls')), 
    path('idea/', include('idea.urls')),
    path('detail/', include('ideaDetail.urls')),
    path('mypage/', include('mypage.urls')),
    path('submit/', include('submit.urls')),
    path('accounts/', include('accounts.urls')),
]
