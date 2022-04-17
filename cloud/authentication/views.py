from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import  UserCreationForm

# Create your views here.

def authentication(request):
    return HttpResponse('authentication ...')

def register(request):
    form=UserCreationForm()
    return  render(request,'users/register.html',{'form':form})