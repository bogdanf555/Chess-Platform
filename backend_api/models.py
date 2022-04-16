from django.db import models

# Create your models here.


class User(models.Model):

    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=50, null=False, blank=False, unique=True)

    fullname = models.CharField(max_length=50, null=False, blank=False)

    password = models.TextField(max_length=256, null=False, blank=False)

    game_rating = models.IntegerField(default=800)

    puzzle_rating = models.IntegerField(default=500)

    games = models.IntegerField(default=0)

    puzzles = models.IntegerField(default=0)

    wins = models.IntegerField(default=0)

    loses = models.IntegerField(default=0)

    draws = models.IntegerField(default=0)

    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    last_updated = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meda:
        db_table = "Users"


class Puzzle(models.Model):

    id = models.AutoField(primary_key=True)

    color = models.CharField(max_length=10, default="white")

    board_state = models.JSONField(null=False, blank=False)

    moves = models.JSONField(null=False, blank=False)

    class Meda:
        db_table = "Puzzles"
