from django.urls import path, include
from .views import ContatosView

urlpatterns = [
    path('contatos/', ContatosView.as_view(), name='home')
]