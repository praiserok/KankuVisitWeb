from django import urls
from django.http import HttpResponse
from django.shortcuts import render, redirect
from matplotlib.style import context
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


def coach(request):
    error = ''
    if request.method == 'POST':
        form = CoachAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            error = 'Введено не коректні дані!'

    coachs = Coach.objects.all()
    form = CoachAddForm()

    context = {
        'forms': form,
        'title': Coach._meta.verbose_name,
        'titles': Coach._meta.verbose_name_plural,
        'data': coachs,
        'error': error,
        'activeCoach': 'active'
    }

    return render(request, 'main/visit/pages/coach.html', context)


def sportsman(request):
    error = ''

    if request.method == 'POST':
        form = SportsmanAddForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Введено не коректні дані!'
    sportsmans = Sportsman.objects.all()
    form = SportsmanAddForm()

    context = {
        'forms': form,
        'title': Sportsman._meta.verbose_name,
        'titles': Sportsman._meta.verbose_name_plural,
        'data': sportsmans,
        'error': error,
        'activeSportsman': 'active',
    }

    return render(request, 'main/visit/pages/sportsman.html', context)


def school(request):
    error = ''
    if request.method == 'POST':
        form = SchoolAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school')
        else:
            error = 'Введено не коректні дані!'

    school = School.objects.all()
    form = SchoolAddForm()

    context = {
        'forms': form,
        'title': School._meta.verbose_name,
        'titles': School._meta.verbose_name_plural,
        'data': school,
        'error': error,
        'activeSchool': 'active'
    }

    return render(request, 'main/visit/pages/school.html', context)


def belt(request):

    error = ''
    if request.method == 'POST':
        form = BeltAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school')
        else:
            error = 'Введено не коректні дані!'
    belt = Belt.objects.all()
    form = BeltAddForm()

    context = {
        'forms': form,
        'title': Belt._meta.verbose_name,
        'titles': Belt._meta.verbose_name_plural,
        'data': belt,
        'error': error,
        'activeBelt': 'active'
    }

    return render(request, 'main/visit/pages/belt.html', context)


def coachEdit(request, coach_id):
    coach = Coach.objects.get(pk=coach_id)
    # form = CoachEditForm()

    if request.method == 'POST':
        # print(request.POST.get())
        coach.first_name = request.POST.get('first_name')
        coach.last_name = request.POST.get('last_name')
        coach.surname = request.POST.get('surname')
        coach.dateBirth = request.POST.get('dateBirth')
        coach.email = request.POST.get('email')
        coach.photo = request.POST.get('photo')
        coach.telephone = request.POST.get('telephone')
        coach.telephone2 = request.POST.get('telephone2')
        coach.belt = request.POST.get('belt')
        coach.information = request.POST.get('information')
        coach.is_active = request.POST.get('is_active')

        coach.save()

    context = {'data': coach}

    return render(request, 'main/visit/templates/edit.html',  context)


def sportsmanEdit(request, sportsman_id):
    sportsman = Sportsman.objects.get(pk=sportsman_id)
    context = {'data': sportsman}

    return render(request, 'main/visit/templates/edit.html',  context)


def schoolEdit(request, school_id):
    return 10


def delete(request, coach_id=0, sportsman_id=0, belt_id=0, school_id=0):
    if coach_id:
        coach = Coach.objects.get(pk=coach_id)
        coach.delete()
    elif sportsman_id:
        sportsman = Sportsman.objects.get(pk=sportsman_id)
        sportsman.delete()
    elif school_id:
        school = School.objects.get(pk=school_id)
        school.delete()
    elif belt_id:
        belt = Belt.objects.get(pk=belt_id)
        belt.delete()
    return redirect(request.META['HTTP_REFERER'])


def about(request):
    return render(request, 'main/about.html')
