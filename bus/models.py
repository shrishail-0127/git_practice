from django.db import models

# Create your models here.


class Bus(models.Model):
    name = models.CharField(max_length=100)
    vehicle_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tyre(models.Model):
    vehicle_id = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model

class Engine(models.Model):
    vehicle_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name