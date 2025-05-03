from django.contrib import admin

# Register your models here.

from .models import Team, Player, Tournament, Match

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Tournament)
@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('matchid', 'tournamentname', 'date', 'team1', 'team2')
