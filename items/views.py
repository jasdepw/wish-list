from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


def index(request):
    return HttpResponse("Main Page")

def detail(request, item):
    return HttpResponse("You're looking at item %s." % item)