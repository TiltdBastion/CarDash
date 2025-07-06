from django.contrib.auth.models import User
from django.test import TestCase
from .models import Car

# Create your tests here.
class GetUserCarsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='<PASSWORD>')
        Car.objects.create(user=self.user, license_plate='GR-668-PG')

    def test_get_user_cars(self):
        cars = Car.objects.for_user(self.user)
        self.assertEqual(len(cars), 1)
        self.assertEqual(cars[0].license_plate, 'GR-668-PG')