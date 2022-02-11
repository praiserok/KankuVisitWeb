from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView
from timetable.forms import TimetableAddForm

from timetable.models import Timetable


class TimetableEditView(UpdateView):
    model = Timetable
    template_name = 'timetable/visit/timetableedit.html'
    form_class = TimetableAddForm
    extra_context = {
        'activeTimetable': 'active'
    }


def timetable(request):

    model = Timetable.objects.all().order_by('group')
    error = ''
    fields = Timetable._meta.fields
    table = Timetable._meta.app_label

    if request.method == 'POST':
        form = TimetableAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('timetable')
        else:
            error = 'Введено не коректні дані!'
    else:
        form = TimetableAddForm()

    context = {
        'forms': form,
        'title': Timetable._meta.verbose_name,
        'titles': Timetable._meta.verbose_name_plural,
        'data': model,
        'fields': fields,
        'table': table,
        'error': error,
        'activeTimetable': 'active'
    }

    return render(request, 'timetable/visit/timetable.html', context)


def timetableDelete(request, slug):

    item = Timetable.objects.get(slug=slug)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
