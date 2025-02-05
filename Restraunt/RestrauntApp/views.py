from django.shortcuts import render,redirect
from .models import Allergies, FoodItem
from .forms import TableBookingForm

# Create your views here.

def book_table_view(request):
    if request.method == "POST":
        form = TableBookingForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')  
    else:
        form = TableBookingForm()

    return render(request, "Book_table.html", {'form': form})

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