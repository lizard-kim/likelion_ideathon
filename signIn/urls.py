from django.urls import path
from .views import signin, logout

urlpatterns = [
    path('', signin, name="signin"),
    path('logout/', logout, name="logout"),
]