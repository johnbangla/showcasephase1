from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address
# Register your models here.
admin.site.register(Item)
admin.site.register(OrderItem)
#admin.site.register(Order, OrderAdmin)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
#admin.site.register(Address, AddressAdmin)
admin.site.register(Address)

