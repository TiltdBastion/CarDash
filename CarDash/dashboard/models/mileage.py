from django.contrib.auth import get_user_model
from django.db import models

class Mileage(models.Model):
    date = models.DateField()
    odometer = models.FloatField()
    car = models.OneToOneField('Car', on_delete=models.CASCADE)

    def get_ordered_mileage(self, carId):
        latest_mileage = self.objects.order_by('-date')