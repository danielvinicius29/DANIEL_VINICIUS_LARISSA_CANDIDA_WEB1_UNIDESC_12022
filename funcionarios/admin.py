from django.contrib import admin
from .models import Funcionario 

class Display(admin.ModelAdmin):
    list_display = ('nome', 'CPF', 'cargo', 'sexo', 'salario')

admin.site.register(Funcionario, Display)