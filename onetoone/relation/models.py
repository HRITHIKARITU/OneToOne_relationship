from django.db import models

# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.place_name} is the place"
    
class Restaurant(models.Model):
    place_restaurant = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True
    )
    serves_idly = models.BooleanField(default=False)
    serves_dosa = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.place_restaurant.place_name} is the Restaurants'place name"

class Waiter(models.Model):
    restaurant_waiter = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name_waiter = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name_waiter} is at {self.restaurant_waiter} restaurant"
    
             