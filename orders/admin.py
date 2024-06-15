from django.contrib import admin

# Register your models here.
from .models import Product, OptionList, Option, Cart, CartItem, Order

admin.site.register(Product)
admin.site.register(OptionList)
admin.site.register(Option)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)