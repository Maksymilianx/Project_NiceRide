from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


# Create your models here.


class Car(models.Model):
    brand_of_car = models.CharField(max_length=64, null=True)
    car_model = models.CharField(max_length=64, default='')
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField(default=0)
    production_year = models.PositiveSmallIntegerField(default=0)
    mileage = models.PositiveIntegerField(default=0)
    engine_capacity = models.FloatField(default=0.0)
    horse_power = models.PositiveSmallIntegerField(default=0)
    country = models.CharField(max_length=64, default='')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    images = models.ImageField(null=True, blank=True)

    COLORS = [
        ('BEIGE', 'Beżowy'),
        ('WHITE', 'Biały'),
        ('BURGUNDY', 'Bordowy'),
        ('BROWN', 'Brązowy'),
        ('BLACK', 'Czarny'),
        ('RED', 'Czerwony'),
        ('PURPLE', 'Fioletowy'),
        ('BLUE', 'Niebieski'),
        ('SILVER', 'Srebrny'),
        ('GRAY', 'Szary'),
        ('GREEN', 'Zielony'),
        ('GOLD', 'Złoty'),
        ('YELLOW', 'Żółty'),
        ('DIFFERENT', 'Inny kolor'),

    ]
    car_color = models.CharField(
        max_length=32,
        default='',
        choices=COLORS,
    )
    TYPE_OF_FUEL = [
        ('PETROL', 'Benzyna'),
        ('DIESEL', 'Diesel'),
        ('PETROL+LPG', 'Benzyna + LPG'),
        ('PETROL+CNG', 'Benzyna + CNG'),
        ('ELECTRIC', 'Elektryczny'),
        ('HYBRID', 'Hybrydowy'),
    ]
    fuel_type = models.CharField(
        max_length=32,
        choices=TYPE_OF_FUEL,
        default='',
    )
    TYPE_OF_CAR = [
        ('SEDAN', 'Sedan'),
        ('COUPE', 'Coupe'),
        ('STATION WAGON', 'Station wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('SPORT-UTILITY VEHICLE (SUV)', 'SUV'),
        ('MINIVAN', 'Minivan'),
    ]
    type = models.CharField(
        max_length=32,
        choices=TYPE_OF_CAR,
        default='',
    )


class Opinions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nick')
    content = models.CharField(max_length=256)
    created = models.DateTimeField(default=timezone.now)
    comment_car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name='comments')


class Messages(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messaged')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
    subject = models.CharField(max_length=128, default='')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class ObserveCar(models.Model):
    followed_by = models.ManyToManyField(User, related_name='favourite', blank=True)
    followed = models.ManyToManyField(Car)


class OfferImage(models.Model):
    car = models.ForeignKey(Car, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.car.brand_of_car
