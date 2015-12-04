# coding: utf-8

from django.shortcuts import render, redirect

from simple_forms.apps.core.models import Person
from simple_forms.apps.core.forms import PersonForm


def home(request):
    persons = Person.objects.all()
    return render(request, 'core/home.html', { 'persons': persons })

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('home')
    else:
        form = PersonForm()
    return render(request, 'core/add_person.html', { 'form': form })
