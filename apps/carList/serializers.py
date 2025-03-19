from rest_framework import serializers
from rest_framework import generics,viewsets

from apps.carList.models import CarAll

class CarAllSerializer(serializers.ModelSerializer):
    class Meta:
        model=CarAll
        fields="__all__"