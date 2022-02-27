from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by("-data_criacao") # order_by("coluna"), o menos = decrescente
    # lista_filmes = Filme.objects.all().order_by("-data_criacao")[0:10] # pegar de zero a 10
    return {"lista_filmes_recentes": lista_filmes} # sempre retornar um dicionário "chave":valor

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by("-visualizaoes")[0:5]
    if lista_filmes:
        filme_destaque = lista_filmes[0] # primeiro item -> filme com mais visualizações
    else:
        filme_destaque = None
    return {"lista_filmes_em_alta": lista_filmes, "filme_destaque": filme_destaque}
