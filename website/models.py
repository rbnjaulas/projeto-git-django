from django.db import models

# Create your models here.
class Funcionario (models.Model):

    nome = models.CharField(
        max_length=255,
        null = False,
        blank = False
    )

    sobrenome = models.CharField(
        max_length=255,
        null = False,
        blank = False
    )

    cpf = models.CharField(
        max_length = 14,
        null = False,
        blank = False
    )

    data_admisao = models.DateField(
        null = False,
        blank = False
    )

    salario = models.DecimalField(
        max_digits = 8,
        decimal_places = 2,
        null = False,
        blank = False
    )

    funcionario = models.Manager()
