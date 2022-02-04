from django.shortcuts import render, redirect
from .forms import CoachForm, SportsmanForm
from .models import Sportsman, Coach, Sportsman


def index(request):
    return render(request, 'main/index.html')


def coach(request):
    error = ''
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('coach')
        else:
            error = 'Форма була не вірною!'

    coachs = Coach.objects.all()
    form = CoachForm()

    context = {
        'forms': form,
        'title': Coach._meta.verbose_name,
        'titles': Coach._meta.verbose_name_plural,
        'data': coachs,
        ''
        'error': error,
    }

    return render(request, 'main/admin/pages/coach.html', context)


def sportsman(request):
    error = ''
    if request.method == 'POST':
        form = SportsmanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sportsman')
        else:
            error = 'Форма була не вірною!'

    sportsmans = Sportsman.objects.all()
    form = SportsmanForm()

    context = {
        'forms': form,
        'title': Sportsman._meta.verbose_name,
        'titles': Sportsman._meta.verbose_name_plural,
        'data': sportsmans,
        'error': error,
    }

    return render(request, 'main/admin/pages/sportsman.html', context)


def about(request):
    return render(request, 'main/about.html')