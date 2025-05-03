from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('match/<int:matchid>/', views.match_detail, name='match_detail'),
    path('player/<str:player_name>/', views.player_detail, name='player_detail'),
    path('team/<str:team_name>/', views.team_detail, name='team_detail'),
    path('search/', views.search, name='search'),
    path('tournament/<str:tournament_name>/', views.tournament_detail, name='tournament_detail'),
]

