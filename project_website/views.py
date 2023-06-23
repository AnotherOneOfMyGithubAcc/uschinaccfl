from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")


def news(request):
    return render(request, "news.html")


def business_directory(request):
    return render(request, "business_directory.html")


def contact(request):
    return render(request, "contact.html")


def about_the_chamber(request):
    return render(request, "about_the_chamber.html")


def executive_board(request):
    return render(request, "executive_board.html")


def events(request):
    return render(request, "events.html")


def event_pictures(request):
    return render(request, "event_pictures.html")


def event_videos(request):
    return render(request, "event_videos.html")


def join_our_chamber(request):
    return render(request, "join_our_chamber.html")


def downloads(request):
    return render(request, "downloads.html")
