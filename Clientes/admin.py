from django.contrib import admin
from .models import Cliente
    
class Display(admin.ModelAdmin):
    fields = ['matricula', 'nome', 'telefone', 'cep', 'rua', 'bairro', 'cidade', 'uf', 'created_date']
    readonly_fields = ['created_date']
    list_display = ['matricula', 'created_date']

admin.site.register(Cliente, Display)