from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, "KP/home.html")


def homeks(request):
    return render(request, "KP/homeks.html")
