from django.urls import path
from . import views
urlpatterns = [
    path('book_table',views.book_table_view,name="book_table")
]