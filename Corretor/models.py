from django.db import models
class Corretor(models.Model):

    comissao = models.IntegerField(max_length=100)
    idCorretor = models.CharField(max_length=100)

    def calcular_Salario(comissao,idCorretor):
        calcular = comissao + idCorretor
        return calcular