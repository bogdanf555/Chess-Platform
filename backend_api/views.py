from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from django.db.utils import IntegrityError

from .models import User
from .serializers import UserSerializer

from .models import Puzzle
from .serializers import PuzzleSerializer


class UsersView(APIView, UpdateModelMixin, DestroyModelMixin):
    def get(self, request, username=None):
        if username:
            try:
                queryset = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response(
                    {"errors": "This username does not match any user."}, status=400
                )

            read_serializer = UserSerializer(queryset)
        else:

            queryset = User.objects.all()
            read_serializer = UserSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = UserSerializer(data=request.data)

        if create_serializer.is_valid():

            try:
                user_object = create_serializer.save()
            except IntegrityError:
                return Response("bad", status=400)
            read_serializer = UserSerializer(user_object)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)

    def put(self, request, username=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"errors": "This user does not exist."}, status=400)

        update_serializer = UserSerializer(user, data=request.data)

        if update_serializer.is_valid():

            user_object = update_serializer.save()
            read_serializer = UserSerializer(user_object)

            return Response(read_serializer.data, status=200)

        return Response(update_serializer.errors, status=400)


class UserLoginView(APIView, UpdateModelMixin, DestroyModelMixin):
    def post(self, request):
        create_serializer = UserSerializer(data=request.data)

        if create_serializer.is_valid():

            user = User.objects.filter(
                username__icontains=create_serializer.data["username"],
                password__icontains=create_serializer.data["password"],
            )

            if not user:
                return Response("bad", status=401)

            return Response("ok", status=201)

        return Response("bad", status=400)


class PuzzleView(APIView, UpdateModelMixin):
    def get(self, request, id=None):

        queryset = Puzzle.objects.all()

        read_serializer = PuzzleSerializer(queryset, many=True)

        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = PuzzleSerializer(data=request.data)

        if create_serializer.is_valid():

            try:
                puzzle_object = create_serializer.save()
            except IntegrityError:
                return Response("Integrity error", status=401)

            read_serializer = PuzzleSerializer(puzzle_object)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)

    def put(self, request, id=None):
        try:
            puzzle = Puzzle.objects.get(id=id)
        except Puzzle.DoesNotExist:
            return Response({"errors": "This puzzle does not exist."}, status=400)

        update_serializer = PuzzleSerializer(puzzle, data=request.data)

        if update_serializer.is_valid():

            puzzle_object = update_serializer.save()
            read_serializer = PuzzleSerializer(puzzle_object)

            return Response(read_serializer.data, status=200)

        return Response(update_serializer.errors, status=400)
