from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('book_table',views.book_table_view,name="book_table"),
    path('Menu/',views.Menu,name="Menu"),
    path('contact/', views.contact, name='contact')
]