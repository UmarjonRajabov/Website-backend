from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PortfolioSerializer
from .models import Portfolio


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all().order_by('created_at')
    serializer_class = PortfolioSerializer