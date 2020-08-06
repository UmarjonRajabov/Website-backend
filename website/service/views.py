from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ServiceSerializer
from .models import Service
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from service.models import Service as ServiceModel
from service.serializers import jwtserializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all().order_by('name')
    serializer_class = ServiceSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class ServiceView(generics.ListCreateAPIView):
    model=get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = ServiceModel.objects.all()
    serializer_class = jwtserializer


'''To Display All Data present in service'''

class Service(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceModel.objects.all()
    serializer_class = jwtserializer

'''To Display The data according the PK value from service data'''

class Detailstodo(generics.RetrieveUpdateDestroyAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = ServiceModel.objects.all()
    serializer_class = jwtserializer