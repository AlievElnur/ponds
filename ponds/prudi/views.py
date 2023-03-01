from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'prudi/base.html'

class Proekti(TemplateView):
    template_name = 'prudi/proekti.html'
