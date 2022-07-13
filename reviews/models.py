from django.db import models
from django.forms import CharField

# Create your models here.
class Review(models.Model):
    user_name = CharField(max_length = 30)
    review_text = CharField(max_length = 1000)