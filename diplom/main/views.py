from django.shortcuts import render, get_object_or_404
from django.http import *
from .models import *
from django.views.generic import  TemplateView

class MainView(TemplateView):
    template_name = "main/index.html"
def index(request):
    return render(request, 'main/index.html', )


def otz_slieder(request):
    def any_view(request):
        otzv = otz.objects.get(id=1)
        return render(request,"index.html", {'otzv': otzv})
