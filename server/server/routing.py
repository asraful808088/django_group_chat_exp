from django.urls import path

from .consumers import AsyncGroupChat

urls_patterns=[
    path('ws/chat/<str:room_name>',AsyncGroupChat.as_asgi())
]