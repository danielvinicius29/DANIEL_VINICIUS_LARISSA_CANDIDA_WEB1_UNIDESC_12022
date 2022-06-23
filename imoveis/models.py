from operator import le
from django.db import models

class Imovei(models.Model):

    ESTADOS = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
    )
    POSSUI = (
    ("S", "Sim"),
    ("N", "Não")
    )
    TIPO = (
    ("C", "Casa"),
    ("A", "Apartamento"),
    ("M", "Mansão"),
    ("K", "Kit Net"),
    )
    STATUS = (
    ("C", "Disponível Para Compra"),
    ("A", "Disponível Para Alugar"),
    ("N", "Disponível Para Negociações"),
    ("I", "Vendido"),
    ("L", "Alugado")
    
    )


    nome_da_residencia = models.CharField(max_length=100)
    matricula = models.IntegerField()
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=ESTADOS, blank=False, null=False)
    tamanho = models.CharField(max_length=100)
    comodos = models.CharField(max_length=100)
    garagem = models.CharField(max_length=1, choices=POSSUI, blank=False, null=False)
    valor = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False)
    
    def __str__(self):
        return self.nome_da_residencia