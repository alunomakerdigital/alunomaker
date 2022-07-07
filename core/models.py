from django.db import models

# INICIO # ############ Meus modelos de teste de funcionamento dos links  #############

class Protototipos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=300)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    def __str__(self):
        return self.nome

class Contato(models.Model):
    email = models.EmailField('email', max_length=80)
    instagram = models.CharField('Instagram', max_length=50)
    twitter = models.CharField('Twitter', max_length=50)
    telefone = models.CharField('Telefone', max_length=20)
    whatsapp = models.CharField('WhatssApp', max_length=20)
    youtube = models.CharField('Youtube', max_length=30)
    def __str__(self):
        return self.email

class Ano(models.Model):
    ANO_CHOICES = (
        ("1º", "1º ano"),
        ("2º", "2º ano"),
        ("3º", "3º ano"),
        ("4º", "4º ano"),
        ("5º", "5º ano"),
        ("6º", "6º ano"),
        ("7º", "7º ano"),
        ("8º", "8º ano"),
        ("9º", "9º ano"),

    )
    ano = models.CharField(max_length=10, choices=ANO_CHOICES, blank=False, null=False)
    def __str__(self):
        return self.ano

# CLASSE MODELO DE LINKS E ACESSO DE DADOS PARA TODAS AS DISCIPLINAS #########
class Disciplina(models.Model):

    materia = models.CharField('Disciplina', max_length=150)
    ano = models.CharField('Ano', max_length=20)
    conteudo = models.TextField('Conteúdos', max_length=500)
    objetivos = models.TextField('Objetivos', max_length=500)
    experimentosRoboticos = models.TextField('Protótipos Robóticos vinculados', max_length=200)

    def __str__(self):
        return self.materia
# FINAL # ############ Meus modelos de teste de funcionamento dos links  #############
#------------------------------------------------------------------------------------#

# INICIO ############### SITE ALUNO MAKER DIGITAL OFICIAL ###############

class BaseCurricular(models.Model):
    AREAS_ESPECIFICAS = (
        ("Linguagens", "Linguagens"),
        ("Matemática", "Matemática"),
        ("Ciências da Natureza", "Ciências da Natureza"),
        ("Ciências Humanas", "Ciências Humanas"),
    )
    baseCurricular = models.CharField("baseCurricular", max_length=340, choices=AREAS_ESPECIFICAS)
    def __str__(self):
        return self.baseCurricular

class Sub_Linguagem(models.Model):
    TIPOS_LINGUAGENS = (
        ("Lingua Portuguesa", "Lingua Portuguesa"),
        ("Artes Visuais", "Artes Visuais"),
        ("Teatro", "Teatro"),
        ("Dança", "Dança"),
        ("Música", "Música"),
        ("Educação Física", "Educação Física"),
        ("Língua Estrangeira", "Língua Estrangeira"),
        )
    nomeSubItemLinguagem = models.CharField("nomeSubItemLinguagem",max_length=50, choices=TIPOS_LINGUAGENS)
    def __str__(self):
        return self.nomeSubItemLinguagem

# SUB ITENS HUMANAS
class Sub_Humanas(models.Model):
    TIPOS_HUMANAS = (
                    ("Geografia", "Geografia"),
                    ("História", "História"),
                    ("Ensino religioso", 'Ensino religioso'),
                    )
    nomeSubItemHumanas = models.CharField("nomeSubItemHumanas", max_length=50, choices=TIPOS_HUMANAS)
    def __str__(self):
        return self.nomeSubItemHumanas

#CLASSES DAS TEMÁTICAS POR ÁREA
class TematicasLinguagem(models.Model):
    tematicasLinguagens = models.CharField("tematicasLinguagens", max_length=200)
    def __str__(self):
        return self.tematicasLinguagens

class TematicasMatematica(models.Model):
    tematicasMatematica = models.CharField("tematicasMatematica", max_length=200)
    def __str__(self):
        return self.tematicasMatematica



############################### MODELO PARA PORTIFOLIO DOS PROTÓTIPOS  ###########################
class NomePrototipo(models.Model):
    nomePrototipo = models.CharField("nomePrototipo", max_length=300)
    def __str__(self):
        return self.nomePrototipo

class NomePortfolio(models.Model):
    nomePortfolio = models.CharField("nomePortfolio", max_length=300)
    def __str__(self):
        return self.nomePortfolio

class Plataforma(models.Model):
    plataformaPrototip = models.CharField("plataformaPrototip", max_length=200)
    def __str__(self):
        return self.plataformaPrototip

class EtapasEnsino(models.Model):
    etapasEnsin = models.CharField("etapasEnsin", max_length=100)
    def __str__(self):
        return self.etapasEnsin


class Portfolio(models.Model):
    nomePortfolio = models.ForeignKey("NomePortfolio", on_delete=models.CASCADE)
    plataformaPrototipo = models.ForeignKey("Plataforma", on_delete=models.CASCADE)
    circuitoPrototipo = models.TextField("circuitoPrototipo", max_length=300)
    sourceCodePrototipos = models.TextField("sourceCodePrototipos", max_length=300)
    materiaisPrototipos = models.TextField("materiaisPrototipos", max_length=300)
    etapasEnsino = models.ForeignKey("EtapasEnsino", on_delete=models.CASCADE)
    tematicaLing = models.ForeignKey("TematicasLinguagem", on_delete=models.CASCADE)
    tematicaMat = models.ForeignKey("TematicasMatematica", on_delete=models.CASCADE)
    creditosReferencia = models.CharField("creditosReferencia", max_length=200)
    creditosAdaptacaoPedagogica = models.CharField("creditosAdaptacaoPedagogica", max_length=200)
    siteReferencia = models.CharField("siteReferencia", max_length=200)
    canalAudioVisual = models.CharField("canalAudioVisual", max_length=200)
    def __str__(self):
        return str(self.nomePortfolio)



# CLASSES DOS CONTEUDOS ANALÍTICO
class ConteudoMatematica(models.Model):
    ano = models.ForeignKey("Ano", on_delete=models.CASCADE)
    tematicaMat = models.ForeignKey("TematicasMatematica", on_delete=models.CASCADE)
    conteudoMat = models.TextField("conteudoMat", max_length=300)
    objetivosMat = models.TextField("objetivosMat", max_length=300)
    habilidadesMatBncc = models.TextField("habilidadesMatBncc", max_length=300)
    portfolio = models.ForeignKey("Portfolio", on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.ano} -- {self.tematicaMat} -- {self.conteudoMat}'

class ConteudoLinguagens(models.Model):
    ano = models.ForeignKey("Ano", on_delete=models.CASCADE)
    linguagens = models.ForeignKey("Sub_Linguagem", on_delete=models.CASCADE)
    tematicaLing = models.ForeignKey("TematicasLinguagem", on_delete=models.CASCADE)
    conteudoLing = models.TextField("conteudoLing", max_length=300)
    objetivosLing = models.TextField("objetivosLing", max_length=300)
    habilidadesLingBncc = models.TextField("habilidadesLingBncc", max_length=300)
    portfolio = models.ForeignKey("Portfolio", on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.ano} ** {self.linguagens} ** {self.conteudoLing} '





################################### INICIO MODELAGEM CURRICULO ####################################

class Conteudos(models.Model):
    #Definindo os anos que serão utilizados
    ANO_CHOICES = (
        ("1º", "1º ano"),
        ("2º", "2º ano"),
        ("3º", "3º ano"),
        ("4º", "4º ano"),
        ("5º", "5º ano"),
        ("6º", "6º ano"),
        ("7º", "7º ano"),
        ("8º", "8º ano"),
        ("9º", "9º ano"),
    )
##

    ano = models.ForeignKey('ano',max_length=10, choices=ANO_CHOICES, on_delete=models.CASCADE, blank=False, null=False)
    area = models.CharField('area', max_length=1, blank=False, null=False)
    conteudo = models.TextField('Conteúdo', max_length=400, )

    def __str__(self):
        return self.conteudo
#git tempo real testando sincronia
#banch teste incluida