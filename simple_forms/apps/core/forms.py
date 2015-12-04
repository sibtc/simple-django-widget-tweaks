# coding: utf-8

from django import forms

from simple_forms.apps.core.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone', 'bio',)
