from django.shortcuts import render
from .models import Exhibition

# Create your views here.

def index(request):
    exhibitions = Exhibition.objects.order_by('-date')
    context = {
        'exhibitions': exhibitions,
    }
    return render(request, 'exhibitions/index.html', context)
