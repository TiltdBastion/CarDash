from django.contrib.auth.models import User
from django.test import TestCase
from .models import Car, Mileage
import datetime

# Create your tests here.
class CarTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='<PASSWORD>')
        car = Car.objects.create(user=self.user, license_plate='GR-668-PG')
        Mileage.objects.create(car=car, odometer=100, date=datetime.date.today())

    def test_get_user_cars(self):
        cars = Car.objects.for_user(self.user)
        self.assertEqual(len(cars), 1)
        self.assertEqual(cars[0].license_plate, 'GR-668-PG')

    def test_get_user_mileages(self):
        cars = Car.objects.for_user(self.user)
        self.assertEqual(len(cars), 1)
        car = cars[0]
        last_mileage = Mileage.objects.for_car(car).last()
        self.assertEqual(last_mileage.odometer, 100)