from django.db import models
class Pessoa(models.Model):

    matricula = models.IntegerField(max_length=100)
    telefone = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.DateField(max_length=8)
    cidade = models.CharField(max_length=100)
    uf = models.IntegerField(max_length=100)
