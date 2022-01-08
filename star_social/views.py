from django.views.generic import TemplateView
from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"
