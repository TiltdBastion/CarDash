from django.contrib import admin

from .models import Mileage, Category, Expense
# Register your models here.

admin.site.register(Mileage)
admin.site.register(Expense)
admin.site.register(Category)