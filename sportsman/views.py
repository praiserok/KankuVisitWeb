from django.shortcuts import render, redirect
from sportsman.forms import SportsmanAddForm

from sportsman.models import Sportsman


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

    return render(request, 'sportsman/visit/sportsman.html', context)


def sportsmanEdit(request, sportsman_id):
    sportsman = Sportsman.objects.get(pk=sportsman_id)
    success = ''
    error = ''

    if request.method == 'POST':
        form = SportsmanAddForm(request.POST)
        if form.is_valid():
            form.update()
        else:
            error = 'Введено не коректні дані! Форма не збережена'
    # sportsmans = Sportsman.objects.all()
    print(sportsman)
    form = SportsmanAddForm()

    # if request.method == 'POST':

    #     sportsman.first_name = request.POST.get('first_name')
    #     sportsman.last_name = request.POST.get('last_name')
    #     sportsman.surname = request.POST.get('surname')
    #     sportsman.dateBirth = request.POST.get('dateBirth')

    #     sportsman.telephone = request.POST.get('telephone')

    #     coach.belt = request.POST.get('belt')
    #     coach.information = request.POST.get('information')
    #     if request.POST.get('is_active') == 'on':
    #         sportsman.is_active = 1
    #     else:
    #         sportsman.is_active = 0
    #     sportsman.save()
    #     success = 'Всі зміни збережено'
    # else:
    #     error = 'Нажаль не вдалось внести зміни'

    context = {'data': sportsman, 'form': form,
               'success': success, 'error': error}

    return render(request, 'sportsman/visit/sportsmanedit.html',  context)


def sportsmanDelete(request, sportsman_id):
    sportsman = Sportsman.objects.get(pk=sportsman_id)
    sportsman.delete()

    return redirect(request.META['HTTP_REFERER'])
