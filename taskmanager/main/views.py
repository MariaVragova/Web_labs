from django.shortcuts import render
from .models import Comment
import json

def main(request):
    return render(request, "main.html")


def aboutme(request):
    return render(request, "aboutme.html")

def aboutme2(request):
    return render(request, "aboutme2.html")

def aboutme3(request):
    return render(request, "aboutme3.html")

def works(request):
    return render(request, "works.html")

def works2(request):
    return render(request, "works2.html")

def order(request):
    return render(request, "order.html")

def reviews(request):
    return render(request, "reviews.html")

def contact(request):
    return render(request, "contact.html")