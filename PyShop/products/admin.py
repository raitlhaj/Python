from django.contrib import admin
from .models import Product,Offer





class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','img')
admin.site.register(Product,ProductAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount','description')

admin.site.register(Offer,OfferAdmin)


