from django.shortcuts import render
from decimal import Decimal

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, OptionList, Option, Cart, CartItem, Order
from .serializers import (ProductSerializer, OptionListSerializer, OptionSerializer, CartSerializer, CartItemSerializer, OrderSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class OptionListViewSet(viewsets.ModelViewSet):
    queryset = OptionList.objects.all()
    serializer_class = OptionListSerializer
    
    def get_queryset(self):
        queryset = OptionList.objects.all()
        product_id = self.request.query_params.get('product')
        if product_id is not None:
            queryset = queryset.filter(product=product_id)
        return queryset
    
    @action(detail=False, methods=['get'])
    def by_product(self, request):
        product_id = request.query_params.get('product')
        if product_id:
            queryset = self.get_queryset().filter(product=product_id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response({"error":"product is required"}, status=400)
    
class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    
    def get_queryset(self):
        queryset = Option.objects.all()
        option_list_id = self.request.query_params.get('option_list')
        if option_list_id is not None:
            queryset = queryset.filter(option_list=option_list_id)
        return queryset
    
    @action(detail=False, methods=['get'])
    def by_option_list(self, request):
        option_list_id = request.query_params.get('option_list')
        if option_list_id:
            queryset = self.get_queryset().filter(option_list=option_list_id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response({"error":"option_list is required"}, status=400)
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = serializer.save()
        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
    
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    def create(self, request, *args, **kwargs):
        cart_id = request.data.get('cart')
        cart = Cart.objects.get(id=cart_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart_item = serializer.save(cart=cart)
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def create(self, request, *args, **kwargs):
        cart_id = request.data.get('cart')
        total_price = request.data.get('total_price')
        
        if not cart_id or not total_price:
            return Response({"error": "Both cart and total_price are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            cart = Cart.objects.get(id=cart_id)
        except:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
        
        order_data = {
            'cart': cart_id,
            'total_price': total_price,
        }
        
        serializer = self.get_serializer(data=order_data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
