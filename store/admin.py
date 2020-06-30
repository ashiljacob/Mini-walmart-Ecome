from django.contrib import admin
from .models import Item,BillItem

# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('item','quantity','price')

admin.site.register(Item)
admin.site.register(BillItem,BillAdmin)

