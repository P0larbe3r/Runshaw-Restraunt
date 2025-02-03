from django.contrib import admin
from .models import table_booking

# Register your models here.
#username=onionboy
#password=onionbhaji
admin.site.register(table_booking)
from .models import Allergies, FoodItem

admin.site.register(Allergies)
admin.site.register(FoodItem)
