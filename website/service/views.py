from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ServiceSerializer
from .models import Service


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceSerializer