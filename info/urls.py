from django.urls import include, path
from rest_framework import routers
from info import views


router = routers.DefaultRouter()
router.register(r'team', views.TeamViewSet)
router.register(r'player', views.PlayerViewSet)
router.register(r'player-stats', views.PlayerStatsViewSet)
router.register(r'matches', views.MatchesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]