from django.db import models
from funcionarios.models import Funcionario
from django.db.models import F

class Administradore(models.Model):

    Funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    comissao = models.IntegerField()
    salario = models.IntegerField()

    
    def __str__(self):
        return self.Funcionario.nome
