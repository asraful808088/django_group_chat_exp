from django.urls import path

from .views import Home

urlpatterns = [
    path('join/<str:room_name>/',Home,name="home")
]
