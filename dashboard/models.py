from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Hotels(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/%Y/%m/%d/', default = 'img/no-img.jpg')
    intro = models.CharField(max_length=200)
    min_price = models.IntegerField()
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class Advantages(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

class Ratings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rate = models.FloatField()
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)