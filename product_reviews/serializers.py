from rest_framework import serializers
from .models import ProductReview

class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['user_name', 'review_text', 'created_at', 'product']
