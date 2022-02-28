# PARA CADA PÁGINA: url, view e um tamplate
from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme, PesquisaFilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view

app_name="filme"

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),  # vazio -> refere-se à home
    path('filmes/', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('pesquisa/', PesquisaFilme.as_view(), name="pesquisafilme"),
    path('login/', auth_view.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editarperfil/', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta')
]
