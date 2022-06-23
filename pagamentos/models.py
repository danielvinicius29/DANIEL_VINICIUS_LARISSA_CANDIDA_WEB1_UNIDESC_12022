from django.db import models
from Clientes.models import Cliente
from imoveis.models import Imovei
from corretores.models import Corretore

class pagamento(models.Model):

    FORMAS = (
    ("C","CHEQUE"),
    ("B","BOLETO"),
    ("D","DEPOSITO"),
    ("T","TRANSFERÊNCIA")
    )
    PARCELAS = (
    ("1", "1x/ Sem Juros"),
    ("2", "2x/ Sem Juros"),
    ("3", "3x/ Sem Juros"),
    ("4", "4x/ Sem Juros"),
    ("5", "5x/ Sem Juros"),
    ("6", "6x/ Sem Juros"),
    ("7", "7x/ Sem Juros"),
    ("8", "8x/ Sem Juros"),
    ("9", "9x/ Sem Juros"),
    ("10", "10x/ Sem Juros"),
    ("11", "11x/ Sem Juros"),
    ("12", "12x/ Sem Juros")
    )

    Valor = models.IntegerField()
    Forma_De_Pagamento = models.CharField(max_length=1, choices=FORMAS, blank=False, null=False)
    Parcelas_Do_Pagamento = models.CharField(max_length=2, choices=PARCELAS, blank=False, null=False)
    Data_Do_Pagamento = models.DateTimeField()
    banco = models.CharField(max_length=15)
    agencia = models.CharField(max_length=15)
    conta = models.CharField(max_length=15)
    Nome_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Corretor = models.ForeignKey(Corretore, on_delete=models.CASCADE)
    Imovel = models.ForeignKey(Imovei, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nome_Cliente.nome