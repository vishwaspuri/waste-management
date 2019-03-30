from django.shortcuts import render, get_object_or_404, redirect
from .models import People,Country,City,Bin,State,Worker
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms


def index(request):
    return render(request, "waste/index.html")

def worker_bin_list(request):
    worker = Worker.objects.get(user=request.user)
    bin = Bin.objects.filter(worker = worker)
    return render(request,'waste/worker_bin_list.html',{'bin':bin})

def worker_bin_detail(request,pk):
    bin = Bin.objects.get(pk=pk)
    return render(request,'waste/worker_bin_detail.html',{'bin':bin})

def bin_detail(request, pk):
	bin=get_object_or_404(Bin, pk=pk)
	return render(request, 'waste/bin_detail.html', {'bin':bin}  )

@login_required
def citizen_bin_list(request):
	citizen=People.objects.get(user=request.user)
	bins=Bin.objects.filter(citizen=citizen)
	return render(request, 'waste/citizen_bin_list.html', {'bins':bins})

@login_required
def new_bin(request):
	if request.method=='POST':
		form=forms.CleanGarbageForm(request.POST)
		if form.is_valid():
			bin=form.save(commit=False)
			bin.author=request.user
			return render(request,'waste/citizen_bin_list.html')	
	else:
		form=forms.CleanGarbageForm()
	return render(request,'waste/new_bin.html', {'form':form})

def garbage_is_collected(request,pk):
	bin=get_object_or_404(Bin,pk=pk)
	bin.garbage_collected()
	bin.save()
	return redirect('worker_bin_list')	