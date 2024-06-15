from rest_framework import serializers
from .models import Product, OptionList, Option, Cart, CartItem, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'category']

class OptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionList
        fields = ['id', 'name', 'selection_type', 'product']
        
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option 
        fields = ['id', 'name', 'surcharge', 'option_list']
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'created_at']
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'price', 'selected_options']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'cart', 'total_price', 'created_at']