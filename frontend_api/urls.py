from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test_vue, name="test/"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("user_page/", views.user_page_view, name="user_page"),
    path("chess_board/", views.chess_board_view, name="chess_board"),
]
