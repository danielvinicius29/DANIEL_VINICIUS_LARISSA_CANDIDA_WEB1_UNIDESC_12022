from django.contrib import admin
from .models import Imovei

class Display(admin.ModelAdmin):
    list_display = ('nome_da_residencia', 'matricula', 'cep', 'valor', 'tamanho', 'uf', 'status', 'tipo')

admin.site.register(Imovei, Display)