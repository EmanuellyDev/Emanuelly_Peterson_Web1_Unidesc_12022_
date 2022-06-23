from django.db import models
class Cliente(models.Model):

    data = models.DateField(max_length=8)

    def manter_Conta(void):
        conta = input('Mantenha sua conta: ')
        return conta

    def consultar_Imoveis(Double):
        consultar = input('Consulte seus Imoveis: ')
        return consultar

    def agendar_Visita(void):
        agendar = input('Agende sua visita: ')
        return agendar