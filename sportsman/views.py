from django.shortcuts import render, redirect
from sportsman.forms import SportsmanAddForm
from sportsman.models import Sportsman
from django.views.generic import DetailView, ListView, UpdateView, FormView
from django.urls import reverse_lazy


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


class SportsmanView(ListView, FormView):
    model = Sportsman
    form_class = SportsmanAddForm
    template_name = 'sportsman/visit/sportsman.html'
    success_url = reverse_lazy('sportsman')
    context_object_name = 'data'
    paginate_by = 25  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Sportsman._meta.fields
        context['table'] = Sportsman._meta.app_label
        context['activeSportsman'] = 'active'
        context['title'] = Sportsman._meta.verbose_name
        context['titles'] = Sportsman._meta.verbose_name_plural

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def sportsman(request):

#     model = Sportsman.objects.all()
#     error = ''
#     fields = Sportsman._meta.fields
#     table = Sportsman._meta.app_label

#     if request.method == 'POST':
#         form = SportsmanAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('sportsman')
#         else:
#             error = 'Введено не коректні дані!'
#     else:
#         form = SportsmanAddForm()

#     context = {
#         'forms': form,
#         'title': Sportsman._meta.verbose_name,
#         'titles': Sportsman._meta.verbose_name_plural,
#         'data': model,
#         'fields': fields,
#         'table': table,
#         'error': error,
#         'activeSportsman': 'active',
#     }

#     return render(request, 'sportsman/visit/sportsman.html', context)


def sportsmanDelete(request, slug):
    item = Sportsman.objects.get(slug=slug)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
