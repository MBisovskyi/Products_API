from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255)
    image = models.CharField(max_length = 10000)
    description = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    inventory_quantity = models.IntegerField()