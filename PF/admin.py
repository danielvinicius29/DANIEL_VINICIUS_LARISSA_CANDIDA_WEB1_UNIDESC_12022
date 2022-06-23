from django.contrib import admin
from .models import Pessoa_Fisica

class Display(admin.ModelAdmin):
    list_display = ('CPF', 'nome', 'RG', 'data_de_nascimento', 'sexo')

admin.site.register(Pessoa_Fisica, Display)