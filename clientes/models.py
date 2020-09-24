from django.db import models

# Create your models here.
class Clientes(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    numero = models.IntegerField()

    complemento = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    municipio = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    estado = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    pais = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

