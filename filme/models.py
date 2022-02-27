from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Poderíamos criar um app de usuários e conectar no settings, e gerenciar por lá, mas o Lira preferiu importar no app
# ... filmes. De ambas as formas é necessário criar uma classe usuario e incluir os campos extras que não estão no
# ... usuário padrão do django

# Create your models here.


# criar o filme
LISTA_CATEGORIAS = ( #(armazenar_no_bd, aparecer_para_usuário)
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
) # tupla de tuplas
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=50, choices=LISTA_CATEGORIAS)
    visualizaoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# criar os episódios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE) # campo da foreign key, e...
    # ... coluna que será criada no bd filmes (episodios)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    def __str__(self):
        return self.filme.titulo + " | " + self.titulo

# criar o usuário
class Usuario(AbstractUser):
    # username, nome, email.. já tem no usuário padrão do django
    filmes_vistos = models.ManyToManyField("Filme") # muitos para muitos, Classe="Filme",