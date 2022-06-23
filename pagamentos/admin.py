from django.contrib import admin
from .models import pagamento
from Clientes.models import Cliente

class Display(admin.ModelAdmin):
    list_display = ('Nome_Cliente', 'Valor', 'Data_Do_Pagamento', 'Forma_De_Pagamento', 'Imovel', 'Corretor')

    def NomeCliente(self, instance):
        return instance.Nome_Cliente.nome
admin.site.register(pagamento, Display)