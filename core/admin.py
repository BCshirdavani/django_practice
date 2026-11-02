from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "age", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)