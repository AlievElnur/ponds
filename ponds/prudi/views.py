import dataclasses
from django.shortcuts import redirect, render
from django.views.generic import *

from .forms import ContactForm
from .models import *

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['phone'])
            print(request.POST.get('url_from'))

            data = {
                'name': form.cleaned_data['name'],
                'phone': form.cleaned_data['phone']
            }
        
            html_body = render_to_string('prudi/contact.html', data)
            msg = EmailMultiAlternatives(subject='Звонок', from_email='elnurik97qw@yandex.ru', to=['elnurik97qw@yandex.ru'])
            msg.attach_alternative(html_body, "text/html")
            msg.send()

    return redirect(request.POST.get('url_from'))


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

