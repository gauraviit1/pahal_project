from django.contrib import admin
from shop.models import Cateogry, Product
from shop.forms import CateogryForm

# Register your models here.\
class CateogryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Cateogry, CateogryAdmin)

class ProductAdmin(admin.ModelAdmin):
    form = CateogryForm
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated',
                    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Product, ProductAdmin)