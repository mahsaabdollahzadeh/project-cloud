from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import centeral
from .serializers import centeralSerializer


# Create your views here.
def centarl(request):
    return HttpResponse('hi ...')

class centeralList(generics.ListAPIView):
    queryset = centeral.objects.all()
    serializer_class = centeralSerializer
