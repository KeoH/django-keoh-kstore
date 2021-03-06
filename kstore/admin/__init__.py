#encoding:utf-8
from django.contrib import admin

from kstore.models import BasicConfiguration, Supplier, Manufacturer, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','quantity', 'price',
                    'cost_price', 'profit_over_sale_admin',
                    'profit_over_cost_admin','stockage_value',
                    'abailability']
    ordering = ['name']
    list_filter = ('name',)


admin.site.register(BasicConfiguration)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Manufacturer)
