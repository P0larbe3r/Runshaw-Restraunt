from django.db import models

# Create your models here.
class table_booking(models.Model):
    small='small'
    medium='medium'
    large='large'
    table_choices=[
        (small,'SMALL'),
        (medium,'MEDIUM'),
       (large,'LARGE')
    ]
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    phone=models.IntegerField()
    guests=models.IntegerField()
    table_size=models.CharField(max_length=40,choices=table_choices)
    table_number=models.IntegerField(default= 0)
    date=models.DateField()
    time=models.TimeField()
    date_create=models.DateField()
    
    #Order_reservation=models.ForeignKey()
    


#Class for allergies
class Allergies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class FoodItem(models.Model):

    Main = "Main"
    Starter = "Starter"
    Dessert = "Dessert"
    Drink = "Drink"

    Category = [

        (Main,'MAIN'),
        (Starter,'STARTER'),
        (Dessert,'DESSERT'),
        (Drink,'DRINK')
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=4)
    allergies = models.ManyToManyField(Allergies)
    category = models.CharField(max_length=7,choices=Category,default='MAIN')

    def __str__(self):
        return f'{self.name} - {self.category}'
