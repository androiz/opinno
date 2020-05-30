from django.contrib import admin

from opinno.apps.starwars.models import Character, CharacterImage


class CharacterImageAdmin(admin.TabularInline):
    model = CharacterImage


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'height', 'mass', 'homeworld']
    filter_horizontal = ('starships',)
    inlines = [CharacterImageAdmin]
