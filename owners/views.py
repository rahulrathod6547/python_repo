from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request


def index(request):
    return HttpResponse("Hello world!")