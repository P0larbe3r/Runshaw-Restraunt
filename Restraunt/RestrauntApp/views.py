from django.shortcuts import render

# Create your views here.

def book_table_view(request):
    return render(request,"Book_table.html",{})