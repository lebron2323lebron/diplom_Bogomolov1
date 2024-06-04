from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def prices(request):
    return render(request, 'main/prices.html')


def cources(request):
    return render(request, 'main/cources.html')


def reiting(request):
    return render(request, 'main/reiting.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def forma(request):
    return render(request, 'main/forma.html', context={"user": request.user})
