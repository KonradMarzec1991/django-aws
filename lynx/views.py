from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "lynx/index.html")


def register(request):
    return render(request, "lynx/register.html")


def my_login(request):
    return render(request, "lynx/my-login.html")


def dashboard(request):
    return render(request, "lynx/dashboard.html")

def profile_management(request):
    return render(request, "lynx/profile-management.html")