from django.shortcuts import render, redirect
from .forms import CoachAddForm
from .models import Coach
from django.views.generic import DetailView, ListView, UpdateView


class CoachEditView(UpdateView):
    model = Coach
    template_name = 'coach/visit/coachedit.html'
    form_class = CoachAddForm
    extra_context = {
        'activeCoach': 'active'
    }


def coach(request):
    model = Coach.objects.all().order_by('-belts')
    error = ''
    fields = Coach._meta.fields
    table = Coach._meta.app_label

    if request.method == 'POST':
        form = CoachAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coach')
        else:
            error = 'Введено не коректні дані:'
    else:
        form = CoachAddForm()

    context = {
        'forms': form,
        'title': Coach._meta.verbose_name,
        'titles': Coach._meta.verbose_name_plural,
        'data': model,
        'fields': fields,
        'error': error,
        'table': table,
        'activeCoach': 'active'
    }

    return render(request, 'coach/visit/coach.html', context)


def coachDelete(request, pk):
    item = Coach.objects.get(pk=pk)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
