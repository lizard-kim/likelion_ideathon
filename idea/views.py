from django.shortcuts import render

def idea(request):
    return render(request, 'idea.html')