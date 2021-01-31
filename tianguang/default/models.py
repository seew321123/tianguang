from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)

class Product(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=10000)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,default=1)

class Scroll(models.Model):
    image = models.CharField(max_length=1000)

class Config(models.Model):
    headerImage = models.CharField(max_length=1000)
    aboutUs = models.CharField(max_length=10000)

class News(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)