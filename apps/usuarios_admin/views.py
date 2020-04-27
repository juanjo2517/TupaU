from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class Registro(TemplateView):
    template_name = 'registro.html'

class Login(TemplateView):
    template_name = 'login.html'