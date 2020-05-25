from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .forms import *

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('idea')
        else:
            return render(request, 'signin.html', {'alert': '이메일 또는 비밀번호를 다시 한 번 확인해주세요!', 'user':user})
    else:
        return render(request, 'signin.html')

# @todo: 나중에 동작 확인 
def logout(request):
    #if request.method == 'POST':
        auth.logout(request)
        return redirect('idea')
    #return redirect('/')