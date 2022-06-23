from django.contrib import admin
from .models import Cheque
from Clientes.models import Cliente


class Display(admin.ModelAdmin):
    list_display = ['Financeira', 'Nome_Cliente', 'Data_Abertura']

    def NomeCliente(self, instance):
        return instance.Nome_Cliente.nome

admin.site.register(Cheque, Display)