from django.contrib import admin

from opinno.apps.starwars.models import RecentlyVisited


@admin.register(RecentlyVisited)
class RecentlyVisitedAdmin(admin.ModelAdmin):
    list_display = ['session', 'url', 'created_at']
