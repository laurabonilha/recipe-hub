from django.urls import path
from django.http import HttpResponse
from recipes.views import home
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
    
]