from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def articles(request):
    return render(request, 'articles.html')

def topics(request):
    return render(request, 'topics.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')
