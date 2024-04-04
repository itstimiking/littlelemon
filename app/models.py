from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=224)
    booking_date = models.DateTimeField()
    no_of_guests = models.IntegerField()
    
    def get_item(self):
        return f'{self.name} : {str(self.no_of_guests)}'

class Menu(models.Model):
    title = models.CharField(max_length=224)
    price = models.FloatField()
    inventory = models.IntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'