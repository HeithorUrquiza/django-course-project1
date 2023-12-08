from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, 'recipes/pages/home.html')

def recipes(req, id):
    return render(req, 'recipes/pages/recipe-view.html')