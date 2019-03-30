from django.shortcuts import render, get_object_or_404, redirect
from .models import People,Country,City,Bin,State,Worker
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    pass
