from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=224)
    booking_date = models.DateTimeField()
    no_of_guests = models.IntegerField()

class Menu(models.Model):
    title = models.CharField(max_length=224)
    price = models.FloatField()
    inventory = models.IntegerField()