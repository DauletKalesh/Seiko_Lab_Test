from django.contrib import admin
from shop.models import Items, Shops, Categories
# Register your models here.


@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop_name',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'category_id', 'price', 'amount',)