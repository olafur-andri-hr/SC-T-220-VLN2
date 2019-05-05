from django.test import TestCase

# Create your tests here.
from .models import Color, Vehicle, Car, Scooter


# class MyTest(TestCase):
#     def setUp(self):
#         self.test_color = Color.objects.create(color="black")
#         Car.objects.create(license_plate="CK565", wheel_count=4,
#                            color=self.test_color, manufacturer="Volvo")

#     def test_color(self):
#         color = Color.objects.all()[0]  # Get first color
#         self.assertEqual(color.color, "Black")
#         self.assertEquals(str(self.test_color), "Black")

#     def test_car(self):
#         car = Car.objects.get(license_plate="CK565")
#         self.assertEquals(car.manufacturer, "Volvo")
#         self.assertEquals(car.color, self.test_color)
