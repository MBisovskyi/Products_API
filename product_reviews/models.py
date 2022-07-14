from django.db import models
from products.models import Product

# Create your models here.
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user_name = models.CharField(max_length = 32)
    review_text = models.TextField()
    created_at = models.DateField(auto_now_add=True)