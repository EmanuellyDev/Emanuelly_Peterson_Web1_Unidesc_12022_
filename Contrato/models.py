from django.db import models
class Contrato(models.Model):

    valor = models.IntegerField(max_length=100)
    dadosCliente = models.CharField(max_length=100)
    dadosCorretor = models.CharField(max_length=100)
    descricaoImovel = models.CharField(max_length=100)
    documentacao = models.CharField(max_length=100)
    clausulaPenal = models.CharField(max_length=100)