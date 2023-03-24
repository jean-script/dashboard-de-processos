from django.contrib import admin
from .models import Processos, LogsDoProcesso

# Register your models here.

class ListandoProcessos(admin.ModelAdmin):
    # display mostrado no django
    list_display = ('id', 'empresa','nome_processo', 'area','publicado')
    list_display_links = ('id', 'nome_processo',)
    search_fields = ('nome_processo',)
    list_filter =('empresa',)
    # campos que podem ser editados 
    list_editable = ('publicado',)
    list_per_page = 5

class ListandoLogsDoProcesso(admin.ModelAdmin):
    list_display = ('processo_nome','data_execucao',)
    search_fields = ('processo_nome',)
    list_filter =('processo_nome','data_execucao',)
    list_per_page = 5


admin.site.register(Processos, ListandoProcessos)
admin.site.register(LogsDoProcesso, ListandoLogsDoProcesso)