from django.db import models
from django.contrib.auth import get_user_model

class CarQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(user=user)

class Car(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    make= models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    vin = models.CharField(max_length=100, blank=True, null=True)
    license_plate = models.CharField(max_length=100)

    objects = CarQuerySet.as_manager()

    def __str__(self):
        return self.license_plate


