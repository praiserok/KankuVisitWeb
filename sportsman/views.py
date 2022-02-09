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
    extra_context = {
        'activeSportsman': 'active'
    }


def sportsman(request):

    model = Sportsman.objects.all().order_by('coach')
    error = ''
    fields = Sportsman._meta.fields
    table = Sportsman._meta.app_label

    if request.method == 'POST':
        form = SportsmanAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sportsman')
        else:
            error = 'Введено не коректні дані!'
    else:
        form = SportsmanAddForm()

    context = {
        'forms': form,
        'title': Sportsman._meta.verbose_name,
        'titles': Sportsman._meta.verbose_name_plural,
        'data': model,
        'fields': fields,
        'table': table,
        'error': error,
        'activeSportsman': 'active',
    }

    return render(request, 'sportsman/visit/sportsman.html', context)


def sportsmanDelete(request, pk):
    item = Sportsman.objects.get(pk=pk)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
