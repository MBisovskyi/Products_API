from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_reviews),
     path('<int:pk>/', views.review_operations),
]