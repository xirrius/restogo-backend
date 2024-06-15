from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category=models.CharField(max_length=100)
    
class OptionList(models.Model):
    name = models.CharField(max_length=255)
    selection_type = models.CharField(max_length=50, choices=[
        ('must_select_one', 'Must Select One'),
        ('can_select_multiple', 'Can Select Multiple or None')
    ])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='option_lists', default=1)
    
class Option(models.Model):
    name = models.CharField(max_length=255)
    surcharge = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    option_list = models.ForeignKey(OptionList, on_delete=models.CASCADE, related_name='options')
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    selected_options = models.ManyToManyField(Option, related_name='cart_items')
    
class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)