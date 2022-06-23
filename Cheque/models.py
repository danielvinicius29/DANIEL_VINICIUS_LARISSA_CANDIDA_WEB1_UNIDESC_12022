from django.db import models
from Clientes.models import Cliente

class Cheque(models.Model):

    Financeira = models.CharField(max_length=100)
    Nome_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Numero = models.CharField(max_length=100)
    Data_Abertura = models.DateTimeField()

    
    def __str__(self):
        return self.Financeira
