# from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.
def home(req):
    recipes = Recipe.objects.all()
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def recipes(req, id):
    return render(req, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })