from django.urls import path
from . import views

# recipes:home e.g
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipe'),
]