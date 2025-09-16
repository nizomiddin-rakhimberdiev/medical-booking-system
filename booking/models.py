from django.db import models

# Create your models here.
class Booking(models.Model):
    user = models.CharField(max_length=100)
    time = models.DateTimeField()
    doctor = models.CharField(max_length=100)