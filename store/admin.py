from django.contrib import admin
from store.models import Products, Variation, ReviewRating

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')
    

admin.site.register(Products, ProductsAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)

