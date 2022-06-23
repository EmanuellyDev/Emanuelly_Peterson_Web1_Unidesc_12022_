from django.db import models
class Cheque(models.Model):

    financeira = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100)
    numero = models.IntegerField(max_length=16)
    dataAbertura = models.DateField(max_length=8)