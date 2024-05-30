from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)

