from django.db import models
class Imovel(models.Model):

    matircula = models.IntegerField(max_length=100)
    rua_imo = models.CharField(max_length=100)
    cep_imo = models.CharField(max_length=100)
    bairro_imo = models.CharField(max_length=100)
    cidade_imo = models.DateField(max_length=8)
    uf_imo = models.CharField(max_length=100)
    tamanho_imo = models.IntegerField(max_length=100)
    comodos_imo = models.CharField(max_length=100)
    garagem_imo = models.CharField(max_length=100)
    valor_imo = models.IntegerField(max_length=100)
    tipo_imo = models.CharField(max_length=100)
    status_imo = models.CharField(max_length=100)



    def incluir_Anuncio(void):
        incluir = input()
        return incluir

    def consultar_Anuncio(Double):
        consultar = input()
        return consultar

    def gerar_Anuncio(void):
        gerar = input()
        return gerar

    def remover_Anuncio(void):
        remover = input()
        return remover
