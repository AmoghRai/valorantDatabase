from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Match, Player, Team, PlayerMatchRating, Tournament

def index(request):
    matches = Match.objects.all().order_by('-date')
    return render(request, 'valorantDatabase/index.html', {'matches': matches})

def match_detail(request, matchid):
    match = get_object_or_404(Match, matchid=matchid)
    team1_players = match.team1.player_set.all()
    team2_players = match.team2.player_set.all()

    team1_ratings = [
        (player, PlayerMatchRating.objects.filter(player=player, match=match).first())
        for player in team1_players
    ]
    team2_ratings = [
        (player, PlayerMatchRating.objects.filter(player=player, match=match).first())
        for player in team2_players
    ]

    return render(request, 'valorantDatabase/match_detail.html', {
        'match': match,
        'team1': match.team1,
        'team2': match.team2,
        'team1_ratings': team1_ratings,
        'team2_ratings': team2_ratings,
    })
def player_detail(request, player_name):
    player = get_object_or_404(Player, playername=player_name)

    matches = Match.objects.filter(
        team1=player.teamname
    ) | Match.objects.filter(
        team2=player.teamname
    )
    matches = matches.order_by('-date')

    ratings = PlayerMatchRating.objects.filter(player=player)
    avg_rating = ratings.aggregate(Avg('rating'))['rating__avg']

    return render(request, 'valorantDatabase/player_detail.html', {
        'player': player,
        'ratings': ratings,
        'avg_rating': avg_rating,
        'matches': matches,
    })
from .models import Team, Player, Match

def team_detail(request, team_name):
    team = get_object_or_404(Team, teamname=team_name)
    players = Player.objects.filter(teamname=team_name)
    matches = Match.objects.filter(team1=team_name) | Match.objects.filter(team2=team_name)
    matches = matches.order_by('-date')

    return render(request, 'valorantDatabase/team_detail.html', {
        'team': team,
        'players': players,
        'matches': matches
    })
def search(request):
    query = request.GET.get('q')
    teams = Team.objects.filter(teamname__icontains=query) if query else []
    players = Player.objects.filter(playername__icontains=query) if query else []
    return render(request, 'valorantDatabase/search_results.html', {
        'query': query,
        'teams': teams,
        'players': players,
    })

def tournament_detail(request, tournament_name):
    tournament = get_object_or_404(Tournament,name=tournament_name)
    
    matches = Match.objects.filter(tournamentname=tournament)
    team_ids = set()
    for match in matches:
        if match.team1_id:
            team_ids.add(match.team1.teamname)
        if match.team2_id:
            team_ids.add(match.team2.teamname)

    # Get unique teams
    teams = Team.objects.filter(teamname__in=team_ids)
    ratings = PlayerMatchRating.objects.filter(match__tournamentname=tournament)
    top_rating = ratings.values('player__playername').annotate(avg_rating=Avg('rating')).order_by('-avg_rating').first()
    
    top_player = None
    if top_rating:
        top_player = Player.objects.get(playername=top_rating['player__playername'])
    leaderboard = (
    PlayerMatchRating.objects
    .filter(match__tournamentname=tournament)
    .values('player__playername')
    .annotate(avg_rating=Avg('rating'))
    .order_by('-avg_rating')[:10]  # Top 10
     )
    return render(request, 'valorantDatabase/tournament_detail.html', {
        'tournament': tournament,
        'teams': teams,
        'top_player': top_player,
        'top_rating': round(top_rating['avg_rating'], 2) if top_rating else None,
	'leaderboard': leaderboard,
    })
