from django.urls import path

from . import views

urlpatterns = [
    path("user/", views.UsersView.as_view(), name="perform_register"),
    path("user/<str:username>/", views.UsersView.as_view()),
    path("perform_login/", views.UserLoginView.as_view(), name="perform_login"),
    path("puzzle/", views.PuzzleView.as_view(), name="puzzle"),
    path("puzzle/<int:id>/", views.PuzzleView.as_view()),
]
