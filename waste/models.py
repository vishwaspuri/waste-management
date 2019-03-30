from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Country(models.Model):
    country_name = models.CharField(max_length=30)
    def __str__(self):
        return self.country_name

class State(models.Model):
    state_name = models.CharField(max_length=30)
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.state_name

class City(models.Model):
    city_name = models.CharField(max_length=30)
    state_name = models.ForeignKey(State, on_delete = models.CASCADE)
    def __str__(self):
        return self.city_name

class People(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    pic = models.ImageField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Worker(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    pic = models.ImageField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Bin(models.Model):
    citizen = models.ForeignKey(People,on_delete=models.CASCADE)
    green_waste = models.IntegerField()
    blue_waste = models.IntegerField()
    time = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.citizen

    def send(self):
        self.time = timezone.now()
        self.save()
