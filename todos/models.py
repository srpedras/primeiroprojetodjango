from django.db import models

# Create your models here.

# criando  a tabela Todo


class Todo(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    dtEntrada = models.DateTimeField(null=True, blank=True)
