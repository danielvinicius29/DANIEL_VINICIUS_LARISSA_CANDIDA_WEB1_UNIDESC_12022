from django.db import models
from imoveis.models import Imovei
from Clientes.models import Cliente

class Agendamento(models.Model):

    Data = models.DateTimeField()
    Local = models.ForeignKey(Imovei, on_delete=models.CASCADE)
    Nome_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nome_Cliente.nome
