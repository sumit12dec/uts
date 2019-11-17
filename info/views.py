from django.http import HttpResponse


from info.models import Team, Player, PlayerStats, Matches

from rest_framework import viewsets
from info.serializers import TeamSerializer, PlayerSerializer, PlayerStatsSerializer, MatchesSerializer



class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('-created_at')
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer

class MatchesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Matches.objects.all()
    serializer_class = MatchesSerializer

