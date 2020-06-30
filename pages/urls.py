from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('game/', views.game, name='game'),
    path('current-exhibition/', views.currentexhibition, name='current-exhibition'),
]
