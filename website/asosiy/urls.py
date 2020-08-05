from django.urls import path, include
from . import views
from portfolio.views import PortfolioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'asosiy', views.AsosiyViewSet)
router.register(r'portfolio', PortfolioViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('asosiy/', views.asosiy_list),
    path('asosiy/<int:pk>/', views.asosiy_detail),
]