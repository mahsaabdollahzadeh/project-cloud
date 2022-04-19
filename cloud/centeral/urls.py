
from django.urls import path
from .import views


app_name='centeral',
urlpatterns = [
    path('', views.centeral, name='centeral'),

]