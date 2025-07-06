from django.contrib.auth import get_user_model
from django.db import models

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)
    car = models.ForeignKey('Car', on_delete=models.PROTECT)

    def __str__(self):
        return self.date.__str__() + ' - ' + self.amount.__str__() + '€'