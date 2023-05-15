from django.contrib import admin
from manga.models import Manga

class MangaAdmin(admin.ModelAdmin):
    search_fields = [
        'name',   
    ]
    list_display = [
          'name',
    ]
    list_filter = [
         'name',
    ]

admin.site.register(Manga,MangaAdmin)