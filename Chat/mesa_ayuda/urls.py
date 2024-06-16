from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # Ruta para la vista principal
    path('chat-response/', views.chat_response, name='chat_response'),  # Ruta para manejar respuestas del chat
]
