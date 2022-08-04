from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView
from timetable.forms import TimetableAddForm

from timetable.models import Timetable


class GroupEditView(LoginRequiredMixin, CustomSuccessMessageMixin, UpdateView):
    model = Group
    template_name = 'group/visit/groupedit.html'
    form_class = GroupAddForm
    success_url = reverse_lazy('group')
    success_msg = Group._meta.verbose_name + ' добавлена успішно!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activeGroup'] = 'active'
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].coach:
            return self.handle_no_permission()
        return kwargs


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
