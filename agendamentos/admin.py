from django.contrib import admin
from .models import Agendamento
from Clientes.models import Cliente


class Display(admin.ModelAdmin):
    list_display = ['Nome_Cliente', 'Data', 'Local']

    def NomeCliente(self, instance):
        return instance.Nome_Cliente.nome
admin.site.register(Agendamento, Display)