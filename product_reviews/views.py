from rest_framework.decorators import api_view
from product_reviews.models import ProductReview
from .serializers import ProductReviewsSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def product_reviews(request, pk):
    if request.method == 'GET':
        reviews = ProductReview.objects.filter(product_id = pk)
        serializer = ProductReviewsSerializer(reviews, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductReviewsSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def review_operations(request, pk):
    review = get_object_or_404(ProductReview, pk = pk)
    if request.method == 'PUT':
        serializer = ProductReviewsSerializer(review, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)