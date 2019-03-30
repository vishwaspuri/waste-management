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

class City(models.Model, Bin):
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
    garbage_is_collected=models.BooleanField(default=False)#True if garbage is collected, False if garbage is yet to be collected
    def garbage_collected(self):#When worker collects the garbage
        self.garbage_is_collected=True
        return garbage_is_collected
    def garbage_to_be_collected(self):#When citizen wants worker to collect garbage
        self.garbage_is_collected=False
        return garbage_is_collected
    def total_garbage(self):#total garbage collected
        total_garbage_collected=(self.green_waste+self.blue_waste)
        return total_garbage_collected
    def __str__(self):
        return self.citizen
    def send(self):
        self.time = timezone.now()
        self.save()
