from django.db import models

class Aviso(models.Model):

    matricula_avi = models.IntegerField(max_length=100)
    assunto_avi = models.CharField(max_length=100)
    data_avi = models.DateField(max_length=8)

    def incluir_aviso(void):
        incluir = input('Inclua seu aviso: ')
        return incluir

    def consultar_aviso(Double):
        consultar = input('Consulte seu aviso: ')
        return consultar

    def remover_aviso(void):
        remover = input('Remova seu aviso: ')
        return remover