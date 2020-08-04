from django.urls import path
from asosiy import views

urlpatterns = [
    
    path('asosiy/', views.asosiy_list),
    path('asosiy/<int:pk>/', views.asosiy_detail),
]