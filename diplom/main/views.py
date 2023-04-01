from django.shortcuts import render, get_object_or_404
from django.http import *
from .models import *


def index(request):
    return render(request, 'main/df.html', )


def otz_slieder(request):
    def any_view(request):
        otzv = otz.objects.get(id=1)
        return render(request,"df.html", {'otzv': otzv})
