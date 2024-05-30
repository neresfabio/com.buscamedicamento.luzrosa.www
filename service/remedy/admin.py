from django.contrib import admin
from .models import RemedyOrder


@admin.register(RemedyOrder)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'value')
    search_fields = ('name',)

