from django.shortcuts import render
from .models import Work

# Create your views here.

def index(request):
    works = Work.objects.all()
    context = {
        'works': works,
    }
    return render(request, 'works/index.html', context)