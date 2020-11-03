from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

class Cliente(ExportModelOperationsMixin('cliente'), models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome
