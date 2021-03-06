from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDeleteAPIView, add_image, delete_image

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:id>/', ProductRetrieveUpdateDeleteAPIView.as_view()),
    path('products/images/', add_image),
    path('products/images/<int:id>/delete/', delete_image)
]