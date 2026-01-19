from lynx.forms import CreateUserForm
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "lynx/index.html")


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")

    context = {"form": form}
    return render(request, "lynx/register.html", context=context)


def my_login(request):
    return render(request, "lynx/my-login.html")


def dashboard(request):
    return render(request, "lynx/dashboard.html")

def profile_management(request):
    return render(request, "lynx/profile-management.html")