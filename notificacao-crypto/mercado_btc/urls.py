from django.urls import path
from . import views

urlpatterns = [
    path('', views.funcaoEnviaMensagem, name = 'index'),
    path('mercado/', views.buscaCotacaoMercadoBtc, name = 'index'),
]