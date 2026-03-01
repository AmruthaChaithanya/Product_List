from django.contrib import admin

from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'catagory', 'stock', 'created_at']
    search_fields = ['name', 'catagory']
    list_filter = ['catagory', 'created_at']

admin.site.register(Product, ProductAdmin)