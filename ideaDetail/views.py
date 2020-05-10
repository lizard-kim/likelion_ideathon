from django.shortcuts import render, redirect
from idea.models import Idea_Comments, Idea_AddComments
from django.utils import timezone

def detail(request):
    
    if request.method == 'POST':

        comment = request.POST.get('comment', 0)
        addcomment = request.POST.get('addcomment', 0)

        if 'comment' in request.POST:
            comment = Idea_Comments()
            comment.text = request.POST['comment']
            comment.create_data = timezone.datetime.now()
            comment.save()

        elif 'addcomment' in request.POST:
            addcomment = Idea_AddComments()
            addcomment.text = request.POST['addcomment']
            addcomment.create_data = timezone.datetime.now()
            addcomment.save()
        
        return redirect('detail')

    else:
        comment_list = Idea_Comments.objects.all()
        addcomment_list = Idea_AddComments.objects.all()

        return render(request, 'detail.html',{
            'comment_list' : comment_list,
            'addcomment_list' : addcomment_list
        })
