from django.contrib import admin
from . import models

admin.actions.delete_selected.short_description = "Удалить"


def yesProduct(modeladmin, request, queryset):
   queryset.update(in_stock=True) 

yesProduct.short_description = "В наличии"

def noProduct(modeladmin, request, queryset):
   queryset.update(in_stock=False) 

noProduct.short_description = "Отсутствует"


def yesOrder(modeladmin, request, queryset):
   queryset.update(complete=True) 

yesOrder.short_description = "Выполнен"

def noOrder(modeladmin, request, queryset):
   queryset.update(complete=False) 

noOrder.short_description = "В процессе"


class NutTypeAdmin(admin.ModelAdmin):
    list_display=('label', 'id')
    search_fields=['label', 'id']
    fields=('id', 'label')
    readonly_fields=('id')

class ProductAdmin(admin.ModelAdmin):
    list_display=('label', 'getNutType', 'the_type', 'getThubmnail', 'count', 'price', 'in_stock', 'id')
    list_filter=('the_type', 'in_stock', 'nut_type__label')
    search_fields=['id', 'label']
    fields=('id', 'getImage', 'image', ('label','the_type', 'nut_type'),('price','count','in_stock'))
    readonly_fields=('id', 'getImage')
    actions=[yesProduct, noProduct]

class OrderAdmin(admin.ModelAdmin):
    list_display=('name', 'phone', 'email', 'company', 'complete', 'id')
    list_filter=('company', 'complete')
    search_fields=['id', 'name']
    fields=('id', ('name','company'),('phone','email','complete'),('street','house','corps','building','number'))
    readonly_fields=('id')
    actions=[yesOrder, noOrder]


admin.site.register(models.NutType, NutTypeAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
