from django.contrib import messages
from django.http import HttpResponseRedirect

# Вивід повідомлень через success_msg


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?slug=%s' % (self.success_url, self.object.slug)
