from django.contrib.auth import get_user_model
from django.db import models

class MileageQuerySet(models.QuerySet):
    def for_car(self, car):
        return self.filter(car=car)

class Mileage(models.Model):
    date = models.DateField()
    odometer = models.FloatField()
    car = models.OneToOneField('Car', on_delete=models.CASCADE)

    objects = MileageQuerySet.as_manager()