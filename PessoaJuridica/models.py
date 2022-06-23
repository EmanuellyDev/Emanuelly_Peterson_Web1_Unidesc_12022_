from django.db import models
class PessoaJuridica(models.Model):

    cnpf = models.CharField(max_length=100)
    razaoSocial = models.CharField(max_length=100)
    representanteLegal = models.CharField(max_length=100)
