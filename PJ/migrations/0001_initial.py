# Generated by Django 4.0.4 on 2022-06-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa_Juridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cnpj', models.CharField(max_length=100)),
                ('Razao_Social', models.CharField(max_length=100)),
                ('Representante_Legal', models.CharField(max_length=100)),
            ],
        ),
    ]