from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import path
from django.contrib import admin


# Create your views here.
def display(request):
    return HttpResponse("<h1>Hola mundo app2</h1>")
