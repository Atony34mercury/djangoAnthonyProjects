from django.db import models

# Create your models here.
class Customer(models.Model):
    customerNumber = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=100)
    email = models.EmailField()
    region = models.CharField(max_length=100)