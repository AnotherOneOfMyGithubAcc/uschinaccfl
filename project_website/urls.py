
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('news/', views.news),
    path('business-directory/', views.business_directory),
    path('contact/', views.contact),
    path('about-the-chamber/', views.about_the_chamber),
    path('executive-board/', views.executive_board),
    path('events/', views.events),
    path('event-pictures/', views.event_pictures),
    path('event-videos/', views.event_videos),
    path('join-our-chamber', views.join_our_chamber),
    path('downloads', views.downloads),
    # path('', views.),
]