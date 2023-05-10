from django.db import models
from .models import *

from django.contrib.auth.models import User


class Foodmenu(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    fimage = models.ImageField(upload_to='pics/')

class Signup(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

class Cart(models.Model):
    username = models.CharField(max_length=128)
    product  = models.CharField(max_length=128)
    quantity = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    image = models.ImageField(upload_to='pics/')
    

class Breakfast(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')


class Lunch(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')

class FastFood(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')
class ComboOffer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')

class FreshJuice(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')

class ChatItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bimage = models.ImageField(upload_to='pics/')

