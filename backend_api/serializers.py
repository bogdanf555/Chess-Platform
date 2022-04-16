from importlib.metadata import requires
from rest_framework import serializers

from .models import User
from .models import Puzzle


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, required=True)
    fullname = serializers.CharField(max_length=50, required=False)
    password = serializers.CharField(max_length=256, required=False)
    puzzles = serializers.IntegerField(required=False)
    puzzle_rating=serializers.IntegerField(required=False)

    def create(self, validated_data):

        return User.objects.create(
            username=validated_data.get("username"),
            fullname=validated_data.get("fullname"),
            password=validated_data.get("password"),
        )

    def update(self, instance, validated_data): 

        instance.puzzle_rating += validated_data.get("puzzle_rating", instance.puzzle_rating)
        instance.puzzles += validated_data.get("puzzles", instance.puzzles)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "fullname",
            "password",
            "game_rating",
            "puzzle_rating",
            "games",
            "wins",
            "loses",
            "draws",
            "puzzles",
        )


class PuzzleSerializer(serializers.ModelSerializer):

    color = serializers.CharField(max_length=10, required=True)
    board_state = serializers.JSONField(required=False)
    moves = serializers.JSONField(required=True)

    def create(self, validated_data):

        return Puzzle.objects.create(
            color=validated_data.get("color"),
            board_state=validated_data.get("board_state"),
            moves=validated_data.get("moves"),
        )

    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the todo item instance in the database
        instance.board_state = validated_data.get("board_state", instance.board_state)
        instance.color = validated_data.get("color", instance.color)
        instance.moves = validated_data.get("moves", instance.moves)
        instance.save()
        return instance

    class Meta:
        model = Puzzle
        fields = (
            "id",
            "color",
            "board_state",
            "moves",
        )
