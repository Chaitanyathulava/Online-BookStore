# models.py in the 'bookstore' app
from django.core.validators import RegexValidator
from django.db import models

class Signup1(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password= models.CharField(max_length=50)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    textarea= models.CharField(max_length=300)

class cart(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.CharField(max_length=200)

class CheckOut(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField(max_length=100)
    nameoncard = models.CharField(max_length=100)
    creditcardnumber = models.IntegerField(max_length=100)
    expmonth = models.CharField(max_length=100)
    expyear = models.IntegerField(max_length=100)
    CVV = models.IntegerField(max_length=100)