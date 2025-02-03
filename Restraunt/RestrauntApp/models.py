from django.db import models

# Create your models here.
class table_booking(models.Model):
    table_choices={
        'small':'SMALL',
        'medium':'MEDIUM',
        'large':'LARGE'
    }
    first_name=models.CharField()
    last_name=models.CharField()
    email=models.EmailField()
    phone=models.IntegerField()
    guests=models.IntegerChoices()
    table_size=models.CharField(40,choices=table_choices)


#Class for allergies
class Allergies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodItem(models.Model):


    Category = (
    ('Main','MAIN'),
    ('Starter','STARTER'),
    ('Dessert','DESSERT'),
    ('Drink','DRINK'),
)
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=4)
    allergies = models.ManyToManyField(Allergies)
    category = models.CharField(max_length=7,choices=Category,default='Main')

    def __str__(self):
        return f'{self.name} - {self.category}'
