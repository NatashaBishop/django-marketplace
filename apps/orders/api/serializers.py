from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.products.api.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "buyer", "created_at", "is_paid", "items"]
        read_only_fields = ["buyer"]

    def create(self, validated_data):
        request = self.context["request"]
        order = Order.objects.create(buyer=request.user)
        return order
