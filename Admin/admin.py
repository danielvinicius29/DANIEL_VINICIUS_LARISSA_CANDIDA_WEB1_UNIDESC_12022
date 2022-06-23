from django.contrib import admin
from .models import Administradore
from funcionarios.models import Funcionario


class Display(admin.ModelAdmin):
    list_display = ['Funcionario', 'salario', 'comissao']

    def NomeCliente(self, instance):
        return instance.Funcionario.nome

admin.site.register(Administradore, Display)