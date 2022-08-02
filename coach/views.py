from django.shortcuts import render, redirect
from .forms import CoachAddForm
from .models import Coach
from django.views.generic import DetailView, ListView, UpdateView, FormView
from django.urls import reverse_lazy


class CoachEditView(UpdateView):
    model = Coach
    template_name = 'coach/visit/coachedit.html'
    form_class = CoachAddForm
    extra_context = {
        'activeCoach': 'active'
    }


class CoachView(ListView, FormView):
    model = Coach
    form_class = CoachAddForm
    template_name = 'coach/visit/coach.html'
    success_url = reverse_lazy('coach')
    context_object_name = 'data'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Coach._meta.fields
        context['table'] = Coach._meta.app_label
        context['activeCoach'] = 'active'
        context['title'] = Coach._meta.verbose_name
        context['titles'] = Coach._meta.verbose_name_plural
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def coachDelete(request, slug):
    item = Coach.objects.get(slug=slug)
    item.delete()

    return redirect(request.META['HTTP_REFERER'])
