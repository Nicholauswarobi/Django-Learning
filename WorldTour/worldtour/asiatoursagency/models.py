from django.db import models

# Create your models here.
class Tour(models.Model):
    # Define the fields for the Tour model
    original_country = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    number_of_nights = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # This is string represantation of tour
    def __str__(self):
        return (f"ID: {self.id}: from {self.original_country} To {self.destination_country}, Number of Days {self.number_of_nights} price cost {self.price} KSH")

