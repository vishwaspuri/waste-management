from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    country_name = models.CharField(max_length=30)

class State(models.Model):
    state_name = models.CharField(max_length=30)
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    city_name = models.CharField(max_length=30)
    state_name = models.ForeignKey(State, on_delete = models.CASCADE)

class People(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    pic = models.ImageField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)

class Worker(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    pic = models.ImageField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)

class Bin(models.Model):
    citizen = models.ForeignKey(People,on_delete=models.CASCADE)
    green_waste = models.IntegerField()
    blue_waste = models.IntegerField()
