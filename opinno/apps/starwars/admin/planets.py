from django.contrib import admin

from opinno.apps.starwars.models import Planet


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ['name', 'diameter', 'terrain', 'population']
