# Generated by Django 4.0.5 on 2022-06-23 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imoveis', '0001_initial'),
        ('Clientes', '0003_cliente_nome'),
        ('corretores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descricao_Imovel', models.TextField()),
                ('Valor', models.IntegerField()),
                ('Documentacao', models.TextField()),
                ('Clausula_Penal', models.CharField(max_length=100)),
                ('Corretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corretores.corretore')),
                ('Imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.imovei')),
                ('Nome_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente')),
            ],
        ),
    ]