from django.shortcuts import render, redirect
from group.forms import GroupAddForm
from group.models import Group

from django.views.generic import DetailView, ListView, UpdateView


class GroupEditView(UpdateView):
    model = Group
    template_name = 'group/visit/groupedit.html'
    form_class = GroupAddForm
    extra_context = {
        'activeGroup': 'active'
    }


def group(request):

    model = Group.objects.all().order_by('coach')
    error = ''
    fields = Group._meta.fields
    table = Group._meta.app_label

    if request.method == 'POST':
        form = GroupAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('group')
        else:
            error = 'Введено не коректні дані!'
    else:
        form = GroupAddForm()

    context = {
        'forms': form,
        'title': Group._meta.verbose_name,
        'titles': Group._meta.verbose_name_plural,
        'data': model,
        'fields': fields,
        'table': table,
        'error': error,
        'activeGroup': 'active'
    }

    return render(request, 'group/visit/group.html', context)


def groupDelete(request, pk):

    item = Group.objects.get(pk=pk)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
