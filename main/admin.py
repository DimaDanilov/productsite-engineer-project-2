from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Brand, ProductGroup, Products, Post, Salerman, Customer, Sale, SaleCheck, Promotion, Delivery


class ProductsAdminSite(admin.ModelAdmin):
    actions = ['zero']
    model = Products
    list_display = ("title", "price")
    fields = ['brand','productGroup','title', 'description', 'price']

    def zero(self, request, queryset):
        row_update = queryset.update(price = 0)

    zero.short_description = "Обнулить"
    zero.allowed_permissions = ('change', )


admin.site.register(Brand)
admin.site.register(ProductGroup)
admin.site.register(Products, ProductsAdminSite)
admin.site.register(Post)
admin.site.register(Salerman)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleCheck)
admin.site.register(Promotion)
admin.site.register(Delivery)