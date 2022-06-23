from django.db import models
class Gerente(models.Model):

    comissao = models.IntegerField(max_length=100)

    def calcular_Salario(Double):
        comissao = int(input('inclua seu agendamento: '))
        idCorretor = input('inclua seu agendamento: ')

        calcular = comissao + idCorretor
        return calcular
