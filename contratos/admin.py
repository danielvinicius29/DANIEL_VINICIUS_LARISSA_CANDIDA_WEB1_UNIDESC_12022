from django.contrib import admin
from .models import contrato
from Clientes.models import Cliente

class Display(admin.ModelAdmin):
    list_display = ('Nome_Cliente', 'Corretor', 'Imovel', 'Valor')

    def NomeCliente(self, instance):
        return instance.Nome_Cliente.nome
admin.site.register(contrato, Display)