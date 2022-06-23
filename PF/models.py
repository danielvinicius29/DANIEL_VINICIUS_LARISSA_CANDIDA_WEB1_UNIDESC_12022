from django.db import models

class Pessoa_Fisica(models.Model):

    SEXO = (
    ("F", "Feminino"),
    ("M", "Masculino"),
    ("?", "Prefiro não informar")
    )

    CPF = models.CharField(max_length=11)
    RG = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False)
    data_de_nascimento = models.DateField()

    def __str__(self):
        return self.nome