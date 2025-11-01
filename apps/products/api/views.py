from rest_framework import viewsets
from apps.products.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet): #Public read-only product API
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
