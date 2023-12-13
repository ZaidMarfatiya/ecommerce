from django.contrib import admin
from restapp.models import Customer, Product, Order, OrderItem


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'email')


class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'weight')


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'order_date')
    inlines = [OrderItemInline]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    list_filter = ('order', 'product')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

