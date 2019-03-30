from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request):
    user = User.objects.get(username = request.user.username)
    return render(request,'Login/profile.html',{'user':user})
