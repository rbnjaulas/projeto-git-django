# Generated by Django 2.0.7 on 2020-09-18 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200917_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='numero',
            field=models.IntegerField(),
        ),
    ]
