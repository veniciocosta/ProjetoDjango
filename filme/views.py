from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# PARA CADA PÁGINA: url, view e um tamplate
# Create your views here.
# def homepage(request):
# return render(request, 'homepage.html')

class Homepage(TemplateView):
    template_name = 'homepage.html'


# def homefilmes(request):
# context = {}
# context['lista_filmes'] = Filme.objects.all()
# return render(request, 'homefilmes.html', context)

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme  # object_list será passado para o html. Lista de objetos.


class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme  # object -> será passado para o html. Passa 1 object para lá

    #contabilizar visualizações
    def get(self, request, *args, **kwargs):
        # descobrir qual o filme ele tá acessando
        filme = self.get_object() # atribuir a variavel filme o get_object() que é a linha do bd
        # somar 1 na coluna vizualizaoes e salvar
        filme.visualizaoes += 1
        filme.save()
        # return -> redireciona o usuário para o a url final
        return super(Detalhesfilme, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar tabela de filmes pegando os filmes cuja categoria é igual a categoria do silme da página (object)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)
        # filmes_relacionados = Filme.objects.filter(categoria=self.object().categoria)[0:3] # pegar apenas 3 filmes
        context['filmes_relacionados'] = filmes_relacionados
        return context

class PesquisaFilme(ListView):
    template_name = "pesquisa.html"
    model = Filme  # mudar model para episódios, caso queira pesquisar por episódios

    def get_queryset(self):
        termo_de_pesquisa = self.request.GET.get('texto_pesquisado')
        # editar object_list antes de passar pra página
        if termo_de_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_de_pesquisa) # __icontains -> filtrar coluna
            return object_list
        else:
            object_list = self.model.objects.all()
            return object_list