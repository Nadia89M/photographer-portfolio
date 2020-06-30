from django.shortcuts import render
from message.models import Message

# Create your views here.


def index(request):
    messages = Message.objects.order_by('-id').reverse()
    context = {
        'messages': messages,
    }
    return render(request, 'pages/index.html', context)


def welcome(request):
    return render(request, 'pages/welcome.html', {})


def game(request):
    return render(request, 'pages/game.html', {})


def currentexhibition(request):
    return render(request, 'pages/current-exhibition.html', {})
