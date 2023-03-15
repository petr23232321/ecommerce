from django.contrib import admin
from carts.models import Cart, CartItem
# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product','cart', 'quantity', 'is_active')

admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
