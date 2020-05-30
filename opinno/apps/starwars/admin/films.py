from django.contrib import admin

from opinno.apps.starwars.models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['episode_id', 'title', 'director']
