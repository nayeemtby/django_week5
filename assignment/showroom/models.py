from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length = 256)
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.brand.name+' - '+self.name


class Transaction(models.Model):
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)


class Comment(models.Model):
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=256)
