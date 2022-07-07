from django.contrib import admin

# Registros dos meus modelos
from .models import *

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

class AnoAdmin(admin.ModelAdmin):
    list_display = ('ano')

class ConteudosAdmin(admin.ModelAdmin):
    list_display = ('ano', 'conteudo')

class ConteudosDetalhes(admin.ModelAdmin):
    list_display = ('ano','conteudo')

class SubLinguagens(admin.ModelAdmin):
    list_display = ("nomeSubItemLinguagem")

class TematicasLinguagemAdmin(admin.ModelAdmin):
    list_display = ("tematicasLinguagens")

class TematicasMatematicaAdmin(admin.ModelAdmin):
    list_display = ("tematicasMatematica")

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("nomePortfolio")

class NomePrototipoAdmin(admin.ModelAdmin):
    list_display = ("nomePrototipo")

class PlataformaAdmin(admin.ModelAdmin):
    list_display = ("plataformaPrototipo")

class EtapaEnsinoAdmin(admin.ModelAdmin):
    list_display = ("etapaEnsin")

class NomePortfolioAdmin(admin.ModelAdmin):
    list_display = ("nomePortfolio")




# visualizações painel admin
admin.site.register(Protototipos, ProdutosAdmin)
admin.site.register(Contato)
admin.site.register(Ano)
admin.site.register(Conteudos, ConteudosDetalhes)
admin.site.register(Sub_Linguagem)
admin.site.register(Disciplina)
admin.site.register(BaseCurricular)
admin.site.register(ConteudoMatematica)
admin.site.register(ConteudoLinguagens)
admin.site.register(TematicasLinguagem)
admin.site.register(TematicasMatematica)
admin.site.register(Portfolio)
admin.site.register(NomePrototipo)
admin.site.register(Plataforma)
admin.site.register(EtapasEnsino)
admin.site.register(NomePortfolio)
