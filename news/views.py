from django.shortcuts import render
from .models import New

# Create your views here.


def index(request):
    news = New.objects.order_by('-id').reverse()
    context = {
        'news': news,
    }
    return render(request, 'news/index.html', context)
