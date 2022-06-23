from django.db import models
from Clientes.models import Cliente
from imoveis.models import Imovei
from corretores.models import Corretore

class contrato(models.Model):

    Nome_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Corretor = models.ForeignKey(Corretore, on_delete=models.CASCADE)
    Imovel = models.ForeignKey(Imovei, on_delete=models.CASCADE)
    Descricao_Imovel = models.TextField()
    Valor = models.IntegerField()
    Documentacao = models.TextField()
    Clausula_Penal = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nome_Cliente.nome