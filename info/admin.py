from django.contrib import admin

from .models import Team, Player, PlayerStats, Matches

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(PlayerStats)
admin.site.register(Matches)