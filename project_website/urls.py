
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about-the-chamber/', views.about_the_chamber),
    path('executive-board/', views.executive_board),
    path('events/', views.events),
    path('event-pictures/', views.event_pictures),
    path('event-videos/', views.event_videos),
    # path('', views.),
    # path('', views.),
    # path('', views.),
    # path('', views.),
]