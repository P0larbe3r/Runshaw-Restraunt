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