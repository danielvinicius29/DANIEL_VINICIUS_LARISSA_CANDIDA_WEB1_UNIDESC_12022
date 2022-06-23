from django.db import models

class Pessoa_Juridica(models.Model):


    Cnpj = models.CharField(max_length=100)
    Razao_Social = models.CharField(max_length=100)
    Representante_Legal = models.CharField(max_length=100)

    def __str__(self):
        return self.Razao_Social