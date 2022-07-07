from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import *

# minhas views da APLICAÇÃO
def index_Old(request):
    disciplinas = Disciplina.objects.all()


    context = {
        'curso' : 'Programando seu próprio WEBSITE com Django FrameWorks',
        'OUTRA' : ' Você está na Index.html --> Django é incrível ...',
        'disciplinas': disciplinas
    }
    return render(request, 'index.html', context)


def index(request):
    #disciplinas = Disciplina.objects.all()
    portfolios = Portfolio.objects.all()

    context = {
        'curso': 'Conheça os robôs desenvolvidos ',
        'OUTRA': ' selecione o protótipo da sua preferência ...',
        'portfolios': portfolios
    }
    return render(request, 'index.html', context)

def contato(request):
    if str(request.user) == 'AnonymousUser':
        teste = 'USUÁRIO NÃO LOGADO '
        return render(request, 'index.html')
    else:
        teste = 'USUÁRIO LOGADOOOOOO'
        return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def objetivos(request):
    return render(request, 'objetivos.html')

def justificativa(request):
    return render(request, 'justificativa.html')

def avaliacao(request):
    return render(request, 'avaliacao.html')

def eventos(request):
    return render(request, 'eventos.html')

# minhas views da APLICAÇÃO PESQUISA
def pesquisa(request):
    return render(request, 'pesquisa.html')

def disciplina(request, pk):
    #discip = Disciplina.objects.get(id=pk)
    discip = get_object_or_404(Disciplina, id=pk)
    context = {
        'disciplina': discip
    }
    return render(request, 'disciplina.html', context)

def portfolio(request, pk):
    portfolioView = get_object_or_404(Portfolio, id=pk)
    context = {
        'portfolio' : portfolioView
    }
    return render(request, 'portfolio.html', context)

# minhas views da APLICAÇÃO ROBÔS DESTAQUES
def roboticaAvancada(request):
    return render(request, 'roboticaAvancada.html')

# minhas views da APLICAÇÃO ROBÓTICA BASICA
def roboticaBasica(request):
    return render(request, 'roboticaBasica.html')

# minhas views da APLICAÇÃO OFICINAS
def oficinas(request):
    return render(request, 'oficinas.html')

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8)', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8)', status=500)


