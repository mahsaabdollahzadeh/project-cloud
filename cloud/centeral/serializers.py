from rest_framework import serializers
from .models import centeral

class centeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = centeral
        pass