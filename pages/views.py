from django.shortcuts import render
from message.models import Message
from welcome.models import Welcome

# Create your views here.


def index(request):
    messages = Message.objects.order_by('-id').reverse()
    context = {
        'messages': messages,
    }
    return render(request, 'pages/index.html', context)


def welcome(request):
    welcomes = Welcome.objects.all()
    context = {
        'welcomes': welcomes,
    }
    return render(request, 'pages/welcome.html', context)


def game(request):
    return render(request, 'pages/game.html', {})


def currentexhibition(request):
    return render(request, 'pages/current-exhibition.html', {})
