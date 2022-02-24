from rest_framework import serializers
from .models import User, Shipment, Payment, Product, Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ["delivery", "destination", "order", "created_at"]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["amount", "fees", "orders", "created_at"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "order", "created_at"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user", "status", "created_at"]