from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Shipment, Payment, Product, Order
from .serializers import ShipmentSerializer, PaymentSerializer, ProductSerializer, OrderSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def _get_object(model, object_id):
    try:
        return model.objects.get(id=object_id)
    except:
        raise Http404
    
class ShipmentViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ShipmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        shipment = _get_object(model=Shipment, object_id=pk)
        serializer = ShipmentSerializer(shipment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        shipment = Shipment.objects.get(id=pk)
        serializer = ShipmentSerializer(instance=shipment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        shipment = Shipment.objects.get(id=pk)
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class PaymentViewSet(viewsets.ViewSet):
    def list(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        payment = _get_object(model=Payment, object_id=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        payment = Payment.objects.get(id=pk)
        serializer = PaymentSerializer(instance=payment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        payment = Payment.objects.get(id=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        product = _get_object(model=Product, object_id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class OrderViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        order = _get_object(model=Order, object_id=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def update(self, request, pk=None):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(instance=order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        order = Order.objects.get(id=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class UserAPIView(APIView):
    

    def create(self, serializer):
        pass