# PARA CADA PÁGINA: url, view e um tamplate

from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme, PesquisaFilme

app_name="filme"

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),  # vazio -> refere-se à home
    path('filmes/', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('pesquisa/', PesquisaFilme.as_view(), name="pesquisafilme")
]
