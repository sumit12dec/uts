from info.models import Team, Player, PlayerStats, Matches
from django.shortcuts import render
from django.db.models import Q


from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

def get_points():
    res = {}
    for team in Team.objects.all():
        wins = Matches.objects.filter(Q(winner=team) & (Q(team1=team) | Q(team2=team))).count()
        played_matches = Matches.objects.filter((Q(team1=team) | Q(team2=team))).count()
        lost = played_matches - wins
        res[(team.id, team.name, played_matches, wins, lost, 0)] = wins
    return sorted(res, key=res.get, reverse=True)

def get_matches(team_id):
    m = Matches.objects.filter(Q(team1=team_id) | Q(team2=team_id))
    return list(m)


def index(request):
    """View function for home page of site."""
  
    teams = Team.objects.values()
    points = get_points()
    print(points)
    context = {'teams': list(teams), 'points': points}


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



def player(request, team_id):
    """View function for home page of site."""

    players = Player.objects.filter(team=team_id)
    matches_played = get_matches(team_id)
    context = {'players': list(players), 'matches': matches_played, 
               'team_id': team_id, 'team_name': players[0].team.name}

    return render(request, 'player.html', context=context)

def player_details(request, team_id, player_id):
    """View function for home page of site."""

    print(team_id, player_id)
    player_details = PlayerStats.objects.filter(player=player_id, player__team_id=team_id)
    context = {'player_details': list(player_details)}
    return render(request, 'player_details.html', context=context)


