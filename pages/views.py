from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {})

def welcome(request):
    return render(request, 'pages/welcome.html', {})

def game(request):
    return render(request, 'pages/game.html', {})