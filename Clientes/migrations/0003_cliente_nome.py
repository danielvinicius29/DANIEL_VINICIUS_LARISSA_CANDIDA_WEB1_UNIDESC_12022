# Generated by Django 4.0.4 on 2022-06-23 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_cliente_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
