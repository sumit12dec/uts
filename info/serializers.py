from django.contrib.auth.models import User, Group
from info.models import Team, Player, PlayerStats, Matches

from rest_framework import serializers


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'logo_uri', 'club_state']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['team', 'first_name', 'last_name', 'image_uri', 'jersey_number', 'country']

class PlayerStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerStats
        fields = ['player', 'matches_count', 'runs_count', 'highest_score', 'fifties_count', 'hundreds_count']


class MatchesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matches
        fields = ['team1', 'team2', 'winner']
    
    def validate(self, data):
    	
    	if data['team1'] == data['team2']:
    		raise serializers.ValidationError('Opponents can not be same.')
   	
    	if data['winner'] not in [data['team1'], data['team2']]:
    		raise serializers.ValidationError('Winner must be one of the teams.')

    	return data




