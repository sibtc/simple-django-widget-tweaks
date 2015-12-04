#coding: utf-8

from django.conf.urls import url
from simple_forms.apps.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add/$', views.add_person, name='add_person'),
]
