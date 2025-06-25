from django.db import models

# Create your models here.
class Mileage(models.Model):
    date = models.DateField()
    odometer = models.FloatField()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.date.__str__() + ' - ' + self.amount.__str__() + '€'