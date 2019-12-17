from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.http import JsonResponse
from django.views.generic.base import View

from django.shortcuts import render


from django.urls import reverse_lazy
from django.views.generic import CreateView

from core.forms import MailForms
from core.models import MailTest


class HomePageView(CreateView):
    model = MailTest
    template_name = 'index.html'
    form_class = MailForms
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx
