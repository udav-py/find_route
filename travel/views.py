from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = "loh"
    return render(request, 'home.html', {'name':name})