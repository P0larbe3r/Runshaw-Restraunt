from django.shortcuts import render
from .models import Allergies, FoodItem

# Create your views here.

def book_table_view(request):
    return render(request,"Book_table.html",{})

def Menu(request):
    Starters = FoodItem.objects.all().filter(category="STARTER")
    Mains = FoodItem.objects.all().filter(category="MAIN")
    Desserts = FoodItem.objects.all().filter(category="DESSERT")
    Drinks = FoodItem.objects.all().filter(category="DRINK")

    return render(request, 'menu.html',{
        'Starters': Starters,
        'Mains': Mains,
        'Desserts': Desserts,
        'Drinks': Drinks,})

def home (request):
    return render(request,"home.html",{})