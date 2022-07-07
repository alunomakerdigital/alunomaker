from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('sobre', sobre, name='sobre o projeto'),
    path('objetivos', objetivos),
    path('justificativa', justificativa),
    path('avaliacao', avaliacao),
    path('eventos', eventos),
    path('pesquisa', pesquisa),
    path('roboticaAvancada', roboticaAvancada),
    path('roboticaBasica', roboticaBasica),
    path('oficinas', oficinas),
    ##
    path('disciplina/<int:pk>', disciplina, name='disciplina'),
    path('portfolio/<int:pk>', portfolio, name='portfolio'),

]