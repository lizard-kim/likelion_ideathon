from django.shortcuts import render, redirect

def detail(request):
    return render(request, 'detail.html')
