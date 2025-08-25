from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse("<h1>Hola mundo</h1>")