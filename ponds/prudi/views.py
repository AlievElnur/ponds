from django.shortcuts import render
from django.views.generic import *
from .models import *


class HomePage(TemplateView):
    template_name = 'prudi/base.html'

class Demo(TemplateView):
    template_name = 'prudi/demo.html'

class FishOpen(ListView):
    model = Fish
    template_name = 'prudi/fish.html'
    context_object_name = 'posts'

class SculpturesOpen(ListView):
    model = Sculptures
    template_name = 'prudi/sculptures.html'
    context_object_name = 'posts'

class ChannelsOpen(ListView):
    model = Channels
    template_name = 'prudi/chanel.html'
    context_object_name = 'posts'

class PlantsOpen(ListView):
    model = Plants
    template_name = 'prudi/plants.html'
    context_object_name = 'posts'

class OtherOpen(ListView):
    model = Other
    template_name = 'prudi/other.html'
    context_object_name = 'posts'
