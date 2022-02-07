from django.shortcuts import render, redirect
from sportsman.forms import SportsmanAddForm

from sportsman.models import Sportsman
from django.views.generic import DetailView, ListView, UpdateView


# class SportsmanEditView(DetailView):
#     model = Sportsman
#     template_name = 'sportsman/visit/sportsmenan_view.html'
#     context_object_name = 'Sportsman'

class SportsmanEditView(UpdateView):
    model = Sportsman
    template_name = 'sportsman/visit/sportsmanedit.html'
    form_class = SportsmanAddForm


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


def sportsmanDelete(request, pk):
    sportsman = Sportsman.objects.get(pk=pk)
    sportsman.delete()

    return redirect(request.META['HTTP_REFERER'])
