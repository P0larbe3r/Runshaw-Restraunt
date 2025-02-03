from django.db import models

# Create your models here.
class table_booking(models.Model):
    small='small'
    medium='medium'
    large='large'
    table_choices={
        (small,'SMALL'),
        (medium,'MEDIUM'),
       (large,'LARGE')
    }
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    phone=models.IntegerField()
    guests=models.IntegerField()
    table_size=models.CharField(max_length=40,choices=table_choices)
    table_number=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    date_create=models.DateField()
    
    #Order_reservation=models.ForeignKey()