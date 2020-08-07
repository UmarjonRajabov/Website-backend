from django.urls import path, include
from rest_framework import routers
from . import views
from service.views import ServiceView, Service, Detailstodo

router = routers.DefaultRouter()
router.register('services', views.ServiceViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', ServiceView.as_view()),
    path('<int:pk>/', Service.as_view()),
]