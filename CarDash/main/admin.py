from django.contrib import admin

from .models import Mileage, Category, Expense, Car
# Register your models here.

admin.site.register(Car)
admin.site.register(Mileage)
admin.site.register(Expense)
admin.site.register(Category)