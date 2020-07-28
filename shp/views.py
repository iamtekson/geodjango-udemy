from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Jamoat


def jamoat(request):
    jamoatData = serialize('geojson', Jamoat.objects.all())
    return HttpResponse(jamoatData, content_type='geojson')


def index(request):
    return render(request, 'index.html')
