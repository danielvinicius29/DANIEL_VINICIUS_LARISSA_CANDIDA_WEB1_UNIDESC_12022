from django.contrib import admin
from .models import Pessoa_Juridica

class Display(admin.ModelAdmin):
    list_display = ('Cnpj', 'Razao_Social', 'Representante_Legal')

admin.site.register(Pessoa_Juridica, Display)