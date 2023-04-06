from django.shortcuts import render, get_object_or_404
from django.http import *
from .models import *
from django.views.generic import  TemplateView

class MainView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self,**kwargs):
       context= super().get_context_data(**kwargs)
       context['my_record']= CoroselReviews.objects.all()
       return context



