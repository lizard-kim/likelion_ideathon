from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('idea')
        else:
            return render(request, 'signin.html', {'alert': '이메일 또는 비밀번호를 다시 한 번 확인해주세요!'})
    else:
        return render(request, 'signin.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('')
    return render(request, 'signin.html')