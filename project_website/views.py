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

