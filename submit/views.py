from django.shortcuts import render, redirect
from django.contrib import auth
'''
import os, sys
from .model import *
'''

def submit(request):
    '''
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        image = request.FILE.get('image')

        newidea = Idea.objects.create(
            title = title,
            contents = contents,
        )

        newimage = Idea_image_storage.objects.create(
            idea = newidea,
            image = image
        )

        return redirect('../')

    else:
    '''
    return render(request, 'submit.html')