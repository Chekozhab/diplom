from django.shortcuts import render, get_object_or_404
from django.http import *
from .models import *
from django.views.generic import  TemplateView

class MainView(TemplateView):
    template_name = "main/index.html"
