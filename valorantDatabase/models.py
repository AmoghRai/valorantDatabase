# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import math
import random
from django.db import models

class Round(models.Model):
    id = models.AutoField(primary_key=True)
    matchid = models.ForeignKey('valorantDatabase.Match', db_column='matchid', on_delete=models.DO_NOTHING)
    roundnumber = models.IntegerField()
    roundendtime = models.DateTimeField()
    roundwinner = models.CharField(max_length=100)

    class Meta:
        db_table = 'Round'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Diffuse(models.Model):
    round = models.ForeignKey(Round, on_delete=models.DO_NOTHING)
    roundnumber = models.IntegerField(blank=True, null=True)
    eventlocation = models.TextField(blank=True, null=True)
    eventtime = models.DateTimeField(blank=True, null=True)
    diffuser = models.ForeignKey('Player', models.DO_NOTHING, db_column='diffuser', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diffuse'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Elimination(models.Model):
    round = models.ForeignKey(Round, on_delete=models.DO_NOTHING)
    roundnumber = models.IntegerField(blank=True, null=True)
    eventlocation = models.TextField(blank=True, null=True)
    eventtime = models.DateTimeField(blank=True, null=True)
    playereliminating = models.ForeignKey('Player', models.DO_NOTHING, db_column='playereliminating', blank=True, null=True)
    playereliminated = models.ForeignKey('Player', models.DO_NOTHING, db_column='playereliminated', related_name='elimination_playereliminated_set', blank=True, null=True)
    assistingplayers = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elimination'


class Match(models.Model):
    matchid = models.AutoField(primary_key=True)
    tournamentname = models.ForeignKey('Tournament', db_column='tournamentname', on_delete=models.DO_NOTHING)
    date = models.DateField()
    team1 = models.ForeignKey('Team', related_name='team1_matches', db_column='team1', null=True, on_delete=models.SET_NULL)
    team2 = models.ForeignKey('Team', related_name='team2_matches', db_column='team2', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'matches'


class Plant(models.Model):
    round = models.ForeignKey(Round, on_delete=models.DO_NOTHING)
    roundnumber = models.IntegerField(blank=True, null=True)
    eventlocation = models.TextField(blank=True, null=True)
    eventtime = models.DateTimeField(blank=True, null=True)
    planter = models.ForeignKey('Player', models.DO_NOTHING, db_column='planter', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plant'


class Player(models.Model):
    playername = models.CharField(primary_key=True, max_length=100)
    teamname = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'


class Playersocialmedia(models.Model):
    playername = models.ForeignKey(Player, models.DO_NOTHING, db_column='playername', blank=True, null=True)
    socialmedialink = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playersocialmedia'


class Playin(models.Model):
    teamname = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamname', blank=True, null=True)
    playername = models.ForeignKey(Player, models.DO_NOTHING, db_column='playername', blank=True, null=True)
    tournamentname = models.ForeignKey('Tournament', models.DO_NOTHING, db_column='tournamentname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playin'

class Team(models.Model):
    teamname = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.teamname
    class Meta:
        managed = False
        db_table = 'teams'


class Teamsocialmedia(models.Model):
    teamname = models.ForeignKey(Team, models.DO_NOTHING, db_column='teamname', blank=True, null=True)
    socialmedialink = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teamsocialmedia'


class Tournament(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    daterange = models.CharField(max_length=100, blank=True, null=True)
    prestige = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournaments'

class PlayerMatchRating(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    match = models.ForeignKey('Match', on_delete=models.CASCADE)
    rating = models.FloatField()

    class Meta:
        unique_together = ('player', 'match')  # prevent duplicate ratings

    def save(self, *args, **kwargs):
        if self.rating is None:
            self.rating = math.sqrt(random.uniform(0, 2))
        super().save(*args, **kwargs)
