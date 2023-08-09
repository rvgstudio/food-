from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(max_length=20)
    Product_Price = models.CharField(max_length=50)
    Product_Image = models.ImageField( upload_to='images' )
    Product_Brand = models.CharField(max_length=50,null=True)
    Product_Description = models.TextField(null=True)

    def __str__(self):
        return self.Product_Name

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Address_type = models.CharField(max_length=50)
    Name = models.CharField(max_length=20)
    Phone = models.IntegerField()
    Apartment = models.CharField(max_length=50)
    Society = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.IntegerField()

    def __str__(self):
        return self.Name


class Contact(models.Model):
    Name= models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Subject = models.CharField(max_length=50)
    Message = models.TextField(max_length=50)

    def __str__(self):
        return self.Name
    
class Slider(models.Model):
    Slider1 = models.ImageField(upload_to="slider")
    Slider2 = models.ImageField(upload_to="slider")
