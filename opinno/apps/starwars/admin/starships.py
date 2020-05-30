from django.contrib import admin

from opinno.apps.starwars.models import Starship


@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'length', 'crew', 'cargo_capability']
