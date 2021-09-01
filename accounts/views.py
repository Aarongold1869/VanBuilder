from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm

# Create your views here.
def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/")
    context = { 
        "form": form,
        "btn_label": "Login",
        "title": "Login"
    }
    return render(request, "accounts/auth.html", context)

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = { 
        "form": None,
        "btn_label": "Logout",
        "title": "Logout"
    }
    return render(request, "accounts/auth.html", context)

def register_view(request, *args, **kwargs):
    form = SignUpForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.refresh_from_db()  # load the profile instance created by the signal
        user = authenticate(
            username=user.username,
            password=form.cleaned_data['password1'],                           
        )
        login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Sign Up",
        "title": "Sign Up"  
    }
    return render(request, "accounts/auth.html", context)
  