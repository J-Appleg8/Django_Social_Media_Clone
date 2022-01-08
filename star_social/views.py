from django.views.generic import TemplateView
from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"


class TestPage(TemplateView):
    template_name = "test.html"


class ThanksPage(TemplateView):
    template_name = "thanks.html"
