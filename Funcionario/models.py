from django.db import models
class Funcionario(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNascimento = models.DateField(max_length=8)
    carteiraTrabalho = models.CharField(max_length=100)
    salario = models.IntegerField(max_length=100)
    pis = models.CharField(max_length=100)


    def consultar_Imoveis(Double):
        imoveis = input()
        return imoveis

    def manter_Anuncio(void):
        anuncio= input()
        return anuncio

    def manter_Cliente(void):
        cliente = input()
        return cliente

    def manter_Funcinario(void):
        funcionario = input()
        return funcionario

    def manter_Agendamento(void):
        agendamento = input()
        return agendamento

    def gerar_Relatorio(void):
        relatorio = input()
        return relatorio

    def calcular_Salario(Double):
        salario = input()
        return salario

