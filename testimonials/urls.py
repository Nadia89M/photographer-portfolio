from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='testimonials'),
    path('<int:testimonial_id>', views.testimonial, name='testimonial'),
]


