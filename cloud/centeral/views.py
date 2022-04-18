from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics ,permissions
from .models import centeral
from .serializers import centeralSerializer


# Create your views here.


class centeralList(generics.ListAPIView):
    queryset = centeral.objects.all()
    serializer_class = centeralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(c=self.request.user)