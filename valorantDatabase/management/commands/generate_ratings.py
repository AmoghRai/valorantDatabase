from django.core.management.base import BaseCommand
from valorantDatabase.models import Match, PlayerMatchRating
import random, math

class Command(BaseCommand):
    help = 'Generate match ratings for all players in each match'

    def handle(self, *args, **kwargs):
        for match in Match.objects.all():
            players = list(match.team1.player_set.all()) + list(match.team2.player_set.all())
            for player in players:
                obj, created = PlayerMatchRating.objects.get_or_create(
                    player=player,
                    match=match,
                    defaults={'rating': math.sqrt(random.uniform(0, 2))}
                )
                if created:
                    self.stdout.write(f'Added rating for {player.playername} in match {match.matchid}')
