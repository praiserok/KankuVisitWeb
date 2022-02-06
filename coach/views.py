from django.shortcuts import render, redirect
from .forms import CoachAddForm
from .models import Coach


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

    return render(request, 'coach/visit/coach.html', context)


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
        if request.POST.get('is_active') == 'on':
            coach.is_active = 1
        else:
            coach.is_active = 0
        coach.save()

    context = {'data': coach}

    return render(request, 'main/visit/pages/coach/coachedit.html',  context)


def coachDelete(request, coach_id):
    coach = Coach.objects.get(pk=coach_id)
    coach.delete()

    return redirect(request.META['HTTP_REFERER'])
