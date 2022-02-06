from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    context = {
        'titles': 'Головна сторінка'
    }
    return render(request, 'main/index.html', context)


def indexVisit(request):
    context = {
        'titles': 'Тренерська'
    }
    return render(request, 'main/visit/index.html', context)


def about(request):
    return render(request, 'main/about.html')
