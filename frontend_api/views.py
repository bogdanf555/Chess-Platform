from django.shortcuts import render

# Create your views here.


def test_vue(request):
    return render(request, "frontend_api/test.html")


def login_view(request):
    return render(request, "frontend_api/login.html")


def register_view(request):
    return render(request, "frontend_api/register.html")


def user_page_view(request):

    return render(
        request, "frontend_api/user_page.html", {"username": request.GET["username"]}
    )


def chess_board_view(request):

    return render(
        request, "frontend_api/chess_board.html", {"username": request.GET["username"]}
    )
