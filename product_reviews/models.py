from xmlrpc.client import Boolean
from django.db import models
from products.models import Product

class ProductReview(models.Model):
    user_name = models.CharField(max_length = 32)
    review_text = models.TextField()
    created_at = models.DateField(auto_now_add = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
