from django.contrib import admin
from .models import Corretore
from funcionarios.models import Funcionario


class Display(admin.ModelAdmin):
    list_display = ['ID_Corretor', 'Funcionario', 'salario', 'comissao']


admin.site.register(Corretore, Display)