from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics ,permissions
from rest_framework.decorators import api_view
from .models import centeral
from .serializers import centeralSerializer
from rest_framework.response import responses


# Create your views here.

@api_view()
def test ():
    return responses({'name':'hi airport'})
#class centeralList(generics.ListAPIView):
   # queryset = centeral.objects.all()
   # serializer_class = centeralSerializer
   # permission_classes = [permissions.IsAuthenticated]

    #def perform_create(self, serializer):
     #   serializer.save(c=self.request.user)