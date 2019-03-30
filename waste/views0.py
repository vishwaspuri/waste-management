from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from waste.models import Worker, People
from waste.forms import PeopleForm, WorkerForm

@login_required
def Peopleform(request):
    form = WorkerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            people = form.save(commit=False)
            people.user = request.user
            people.save()
            return render(request,'waste/index.html')
    else:
        return render(request,'Login/user_form.html',{'form':form})

@login_required
def Workerform(request):
    form = WorkerForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            worker = form.save(commit=False)
            worker.user = request.user
            worker.save()
            return render(request,'waste/index.html')
    else:
        return render(request,'Login/user_form.html',{'form':form})

@login_required
def user_profile(request):
    if People.objects.filter(user=request.user):
        user = People.objects.get(user=request.user)
    elif Worker.objects.filter(user=request.user):
        user = Worker.objects.get(user=request.user)
    else:
        user = User.objects.get(username = request.user.username)
    return render(request,'Login/profile.html',{'user':user})
