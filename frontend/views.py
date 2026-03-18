from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StyledSignUpForm

def index(request):
    return render(request, 'index.html')

@login_required
def articles(request):
    return render(request, 'articles.html')

@login_required
def topics(request):
    return render(request, 'topics.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def sign_up(request):
    # Initially get the form to display for the user
    if request.method == "GET":
        form = StyledSignUpForm()
        return render(request, "registration/sign_up.html", {"form": form})
    # After user submits form, save the user and display a message
    if request.method == "POST":
        form = StyledSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have signed up for The Bilal successfully.")
        else:
            messages.error(request,"There was an error when signing up, please check the fields.",)
        return render(request, "registration/sign_up.html", {"form": form})

def forgot_password(request):
    return render(request, 'registration/forgot_password.html')