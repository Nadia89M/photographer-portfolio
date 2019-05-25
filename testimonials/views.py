from django.shortcuts import get_object_or_404, render
from .models import Testimonial

# Create your views here.

def index(request):
    testimonials = Testimonial.objects.order_by('-id').reverse()
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'testimonials/testimonials.html', context)

def testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    context = {
        'testimonial' : testimonial
    }
    return render(request, 'testimonials/testimonial.html', context)
