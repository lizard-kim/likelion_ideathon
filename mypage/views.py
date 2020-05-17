from django.shortcuts import render

def mypage(request):
    return render(request, 'mypage.html')

def edit(request):
    return render(request, 'mypageedit.html')