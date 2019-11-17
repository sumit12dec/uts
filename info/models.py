from django.db import models
from rest_framework import serializers

class Team(models.Model):
    name = models.CharField(max_length=200)
    logo_uri = models.URLField(max_length=400)
    club_state = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    image_uri = models.URLField(max_length=400)
    jersey_number = models.IntegerField(default=0)
    country = models.CharField(max_length=200)

    def __str__(self):
        return "{}: {}".format(self.team, self.first_name)

class PlayerStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    matches_count = models.IntegerField(default=0)
    runs_count = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=0)
    fifties_count = models.IntegerField(default=0)
    hundreds_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}: {} {}".format(self.player.team, self.player.first_name, self.player.last_name)

class Matches(models.Model):

    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name='winner', on_delete=models.CASCADE)

    def __str__(self):
        return self.team1.name + ' v/s ' + self.team2.name + ' [' + self.winner.name + ']' 



