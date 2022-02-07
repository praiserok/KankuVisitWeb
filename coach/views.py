from django.shortcuts import render, redirect
from .forms import CoachAddForm
from .models import Coach
from django.views.generic import DetailView, ListView, UpdateView


class CoachEditView(UpdateView):
    model = Coach
    template_name = 'coach/visit/coachedit.html'
    form_class = CoachAddForm


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


def coachDelete(request, pk):
    coach = Coach.objects.get(pk=pk)
    coach.delete()

    return redirect(request.META['HTTP_REFERER'])
