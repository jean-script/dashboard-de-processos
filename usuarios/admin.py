from django.contrib import admin
from usuarios.models import Profile

# Register your models here.


class ListandoProfile(admin.ModelAdmin):
    # display mostrado no django
    list_display = ('id','usuario','empresa',)
    list_display_links = ('usuario',)
    search_fields = ('usuario','empresa')
    list_filter =('usuario','empresa',)
    list_per_page = 5

admin.site.register(Profile, ListandoProfile)