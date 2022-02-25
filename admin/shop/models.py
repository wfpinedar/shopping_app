from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    status = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    amount = models.IntegerField()
    fees = models.IntegerField()
    orders = models.ManyToManyField(Order)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Shipment(models.Model):
    delivery = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    order = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
