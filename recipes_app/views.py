from django.shortcuts import render

def home(request):
    return render(request, 'recipes_app/home.html')
