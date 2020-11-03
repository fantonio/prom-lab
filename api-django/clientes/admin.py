from django.contrib import admin
from clientes.models import Cliente

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf')
    list_display_links = ('id', 'nome')
    search_fields = ('nome','cpf',)
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Cliente, Clientes)
