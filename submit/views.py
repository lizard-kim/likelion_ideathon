from django.shortcuts import render, redirect
from django.contrib import auth
from idea.models import *

def submit(request):
    if request.method == 'POST':
        title = request.POST['title']
        #contents = request.POST['contents']
        #image = request.FILE.get('image')

        newidea = Idea.objects.create(
            idea_title = title,
        )
        newimage = Idea_image_storage.objects.create(
            idea = newidea,
            #image = image
        )
        #return render(request, 'submit.html')
        
        return redirect('../')

    else:
        return render(request, 'submit.html')
