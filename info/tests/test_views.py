import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Team, Player
from ..serializers import TeamSerializer, PlayerSerializer

# initialize the APIClient app
client = Client()

class GetAllTeamTest(TestCase):
    """ Test module for GET all Team API """

    def setUp(self):
        Team.objects.create(
            name='Casper1', logo_uri="https://hello.com/1.png", club_state='State1')
        Team.objects.create(
            name='Casper2', logo_uri="https://hello.com/2.png", club_state='State2')
        Team.objects.create(
            name='Casper3', logo_uri="https://hello.com/3.png", club_state='State3')
        Team.objects.create(
            name='Casper4', logo_uri="https://hello.com/4.png", club_state='State4')

    def test_get_all_teams(self):
        # get API response
        response = client.get(reverse('team-list'))
        # get data from db
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.data['results'], serializer.data[::-1])
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class CreateNewTeamTest(TestCase):
    """ Test module for inserting a new Team """

    def setUp(self):
        self.valid_payload = {
            'name': 'RCB',
            'logo_uri': "https://hello.com/1.jpg",
            'club_state': 'KA'
        }

        self.invalid_payload = {
            'name': 'RCB',
            'logo_uri': "",
            'club_state': 'KA'
        }

    def test_create_valid_team(self):
        response = client.post(
            reverse('team-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('team-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetAllPlayerTest(TestCase):
    """ Test module for GET all Team API """

    def setUp(self):
        Team.objects.create(
            name='Casper1', logo_uri="https://hello.com/1.png", club_state='State1')
        Player.objects.create(team_id=1,
            first_name='P1 first_name', last_name='P1 last_name', 
            image_uri="https://hello.com/player1.png", jersey_number=1, country='India')
        Player.objects.create(team_id=1,
            first_name='P2 first_name', last_name='P2 last_name',
            image_uri="https://hello.com/player2.png", jersey_number=2, country='South Africa')
        Player.objects.create(team_id=1,
            first_name='P3 first_name', last_name='P3 last_name', 
            image_uri="https://hello.com/player3.png", jersey_number=3, country='Australia')
        Player.objects.create(team_id=1,
            first_name='P4 first_name', last_name='P4 last_name', 
            image_uri="https://hello.com/player4.png", jersey_number=4, country='England')

    def test_get_all_players(self):
        # get API response
        response = client.get(reverse('player-list'))
        # get data from db
        players = Player.objects.all()
        from rest_framework.request import Request

        from rest_framework.test import APIRequestFactory

        factory = APIRequestFactory()
        request = factory.get('/team')


        serializer_context = {
            'request': Request(request),
        }
        serializer = PlayerSerializer(players, many=True, context=serializer_context)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)