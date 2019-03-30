from django.shortcuts import render, get_object_or_404, redirect
from .models import People,Country,City,Bin,State,Worker
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, "waste/index.html")

def worker_bin_list(request):
    worker = Worker.objects.get(user=request.user)
    bin = Bin.objects.filter(worker = worker)
    return render(request,'waste/worker_bin_list.html',{'bin':bin})

def worker_bin_detail(request,pk):
    bin = Bin.objects.get(pk=pk)
    return render(request,'waste/worker_bin_detail.html',{'bin':bin})
