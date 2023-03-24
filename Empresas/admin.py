from django.contrib import admin
from .models import Empresa
# Register your models here.


class ListandoEmpresa(admin.ModelAdmin):
    # display mostrado no django
    list_display = ('id', 'nome_empresa')
    list_display_links = ('id', 'nome_empresa',)
    search_fields = ('nome_empresa',)
    list_filter =('nome_empresa',)
    list_per_page = 5

admin.site.register(Empresa, ListandoEmpresa)
