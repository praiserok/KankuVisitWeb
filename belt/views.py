from django.shortcuts import render, redirect
from belt.models import Belt
from .forms import BeltAddForm
from django.views.generic import DetailView, ListView, UpdateView


class BeltEditView(UpdateView):
    model = Belt
    template_name = 'belt/visit/beltedit.html'
    form_class = BeltAddForm
    extra_context = {
        'activeBelt': 'active'
    }


def belt(request):

    error = ''
    if request.method == 'POST':
        form = BeltAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('belt')
        else:
            error = 'Введено не коректні дані!'

    belt = Belt.objects.all()
    form = BeltAddForm()
    fields = Belt._meta.fields
    table = Belt._meta.app_label

    context = {
        'forms': form,
        'title': Belt._meta.verbose_name,
        'titles': Belt._meta.verbose_name_plural,
        'data': belt,
        'fields': fields,
        'table': table,
        'error': error,
        'activeBelt': 'active'
    }

    return render(request, 'belt/visit/belt.html', context)


def beltDelete(request, pk):

    item = Belt.objects.get(pk=pk)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
