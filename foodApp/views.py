from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def item(request):
    return HttpResponse("This is an item view")

def menu(request):
    return HttpResponse("<h1>This is the menu <h1/>")