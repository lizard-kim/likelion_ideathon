from django.shortcuts import render, redirect
from django.contrib import auth
from idea.model import *

def submit(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']

        newidea = Idea.objects.create(
            title = title,
            contents = contents,
        )
        return redirect('../')

    else:
        return render(request, 'submit.html')