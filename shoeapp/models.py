from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=12)
    usertype = models.CharField(max_length=50, null=1)
    option = (("male", "male"),
               ("female", "female"))
    status=models.CharField(max_length=120,choices=option,default="male")
    date=models.DateField(auto_now=True)

class Categories(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=120)
    details=models.CharField(max_length=120)

class Sizes(models.Model):
    id=models.AutoField(primary_key=True)
    options=(("european_size","european_size"),
            ("american_size","american_size"))
    status=models.CharField(max_length=120,choices=options,default="european_size")

class Color(models.Model):
    id=models.AutoField(primary_key=True)
    color=models.CharField(max_length=120)
    details=models.CharField(max_length=120)

class Style(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=120)
    details=models.CharField(max_length=120)
    image=models.ImageField(upload_to="images")

class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=120)
    details=models.CharField(max_length=120)
    image=models.ImageField(upload_to="images")

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=120)
    details = models.CharField(max_length=120)
    image=models.ImageField(upload_to="images")
    amount=models.IntegerField()
    mrp=models.IntegerField()
    category_id=models.IntegerField()
    size_id=models.IntegerField()
    color_id=models.IntegerField()
    brand_id=models.IntegerField()
    style_id=models.IntegerField()
    options=(("available","available"),
            ("outofstock","outofstock"))
    status=models.CharField(max_length=120,choices=options,default="available")
    date=models.DateField(auto_now=True)

class Cart(models.Model):
    product_id=models.IntegerField()
    user_id=models.IntegerField()
    options=(("ordernotplaced","ordernotplaced"),
            ("orderplaced","orderplaced"))
    status=models.CharField(max_length=120,choices=options,default="ordernotplaced")

class Orders(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.IntegerField()
    user_id=models.IntegerField()
    count=models.IntegerField()
    time=models.TimeField(auto_now=True)
    address=models.CharField(max_length=120)
    option=(("ordered","ordered"),
             ("packed","packed"),
             ("shipped","shipped"),
             ("delivered","delivered"),
             ("cancelled","cancelled"))
    status=models.CharField(max_length=120,choices=option,default="ordered")
    date=models.DateField(auto_now=True)

class Feedback(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.IntegerField()
    order_id=models.IntegerField()
    rating=models.IntegerField()
    option=(("extremelysatisfied","extremelysatisfied"),
            ("extremelydissatisfied","extremelydissatisfied"))
    status=models.CharField(max_length=120,choices=option,default="extremelysatisfied")
    date=models.DateField(auto_now=True)