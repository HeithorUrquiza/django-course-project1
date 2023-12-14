# from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe

# Create your views here.
def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(req,category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
    
    return render(req, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - CATEGORY '
    })

def recipes(req, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    return render(req, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
    
def search(req):
    return render(req, 'recipes/pages/search.html')