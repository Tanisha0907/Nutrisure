from django.db import models

# Create your models here.
class Person(models.Model):
    USER_TYPES = (
        ('Admin', 'admin'),
        ('User', 'user'),
    )
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=5, choices=USER_TYPES)
    user_name = models.CharField(max_length=10, unique=True)
    age = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=254, unique=True)
    mobile_no = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=20)
    password = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.user_name + self.password

class User(Person):
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
    pass

    def __str__(self):
        return self.age + self.breakfast + self.lunch + self.dinner

class Category(models.Model):
    category = models.PositiveIntegerField(primary_key=True)
    lowerbound = models.PositiveBigIntegerField(unique=True)
    upperbound = models.PositiveBigIntegerField(unique=True)

class Food_Item(models.Model):
    CATEGORY_TYPES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    Users = models.ManyToManyField(User)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE , choices=CATEGORY_TYPES)
    calories = models.FloatField()
    proteins = models.FloatField()
    fat = models.FloatField()

class Suggested_Food_Item(models.Model):
    Users = models.ManyToManyField(User)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    calories = models.FloatField()
    proteins = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    fullname = models.CharField(max_length=20,null=True)
    feedback = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.fullname + " " + self.feedback

