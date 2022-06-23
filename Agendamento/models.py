from django.db import models

class Agendamento(models.Model):

    dia= models.DateField(max_length=2)
    hora = models.DateField(max_length=6)
    local = models.DateField(max_length=100)

    def __str__(self):
        return self.dia

    def incluir_Agendamento(void):
        incluir = input('inclua seu agendamento: ')
        return incluir

    def consultar_Agendamento(double):
        consultar = input('consulte seu agendamento: ')
        return  consultar

    def alterar_Agendamento(void):
        alterar = input('altere seu agendamento: ')
        return alterar

    def remover_Agendamento(void):
        remover = input('remova seu agendamento: ')
        return remover