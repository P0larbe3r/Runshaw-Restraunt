from django.shortcuts import render
from .models import Allergies, FoodItem

# Create your views here.

def book_table_view(request):
    return render(request,"Book_table.html",{})

def Menu(request):
    Starters = FoodItem.objects.filter(category="Starter")
    Mains = FoodItem.objects.filter(category="Main")
    Desserts = FoodItem.objects.filter(category="Dessert")
    Drinks = FoodItem.objects.filter(category="Drink")

    return render(request, 'menu.html',{
        'Starters': Starters,
        'Mains': Mains,
        'Desserts': Desserts,
        'Drinks': Drinks,})

def home (request):
    return render(request,"home.html",{})