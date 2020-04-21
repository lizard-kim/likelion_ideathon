from django.shortcuts import render

def submit(request):
    return render(request, 'submit.html')