from django.shortcuts import render
from .models import Tearsheet 

# Create your views here.

def index(request):
    tearsheets = Tearsheet.objects.all()
    context = {
        'tearsheets': tearsheets,
    }
    return render(request, 'tearsheets/index.html', context)
