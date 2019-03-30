from django.contrib import admin
from .models import People,Country,City,Bin,State,Worker

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(People)
admin.site.register(Worker)
admin.site.register(Bin)
# Register your models here.
