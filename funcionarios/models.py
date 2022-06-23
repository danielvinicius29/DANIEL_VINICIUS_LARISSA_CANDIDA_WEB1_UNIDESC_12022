from django.db import models

class Funcionario(models.Model):

    CARGOS = (
    ("G","GERENTE"),
    ("C","CORRETOR"),
    ("A","ADMINISTRADOR")
    )
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
    CTPS = models.CharField(max_length=15)
    salario = models.IntegerField()
    pis = models.CharField(max_length=20)
    cargo = models.CharField(max_length=1, choices=CARGOS, blank=False, null=False)

    def __str__(self):
        return self.nome