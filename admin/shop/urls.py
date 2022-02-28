from django.contrib import admin
from django.urls import path
from .views import ShipmentViewSet, PaymentViewSet, ProductViewSet, OrderViewSet 

urlpatterns = [
    path('shipment', ShipmentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('shipment/<str:pk>', ShipmentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('payment', PaymentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('payment/<str:pk>', PaymentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('product', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('product/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('order', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='order'),
    path('order/<str:pk>', OrderViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='get_delete_update_orders')
]