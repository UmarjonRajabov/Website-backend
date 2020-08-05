from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'text','picture')