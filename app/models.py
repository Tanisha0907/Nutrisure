from django.db import models

# Create your models here.
class Person(models.Model):
    USER_TYPES = (
        ('Admin', 'admin'),
        ('User', 'user'),
    )
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=5, choices=USER_TYPES)
    user_name = models.CharField(max_length=10)
    age = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=254)
    mobile_no = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

class User(models.Model):
    GENDERS = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'others'),
    )
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    breakfast = models.CharField(max_length=10)
    lunch = models.CharField(max_length=10)
    dinner = models.CharField(max_length=10)

class Food_Item(models.Model):
    CATEGORY_TYPES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    category = models.PositiveBigIntegerField(choices=CATEGORY_TYPES)
    calories = models.FloatField()
    proteins = models.FloatField()
    fat = models.FloatField()

class Suggested_Food_Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    calories = models.FloatField()
    proteins = models.FloatField()
    fat = models.FloatField()

class Category(models.Model):
    category = models.PositiveBigIntegerField()
    lowerbound = models.PositiveBigIntegerField()
    upperbound = models.PositiveBigIntegerField()

class Feedback(models.Model):
    fullname = models.CharField(max_length=20,null=True)
    feedback = models.CharField(max_length=50,null=True)

