from django.urls import path
from .consumers import ClockConsumer

websocket_urlpatterns = [
    path("ws/socketclock/", ClockConsumer.as_asgi()),
]