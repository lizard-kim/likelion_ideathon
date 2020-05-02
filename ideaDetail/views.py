from django.shortcuts import render, redirect
from ideaDetail.models import Comment, AddComment
from django.utils import timezone

def detail(request):
    
    if request.method == 'POST':

        comment = request.POST.get('comment', 0)
        addcomment = request.POST.get('addcomment', 0)

        if 'comment' in request.POST:
            comment = Comment()
            comment.text = request.POST['comment']
            comment.create_data = timezone.datetime.now()
            comment.save()

        elif 'addcomment' in request.POST:
            addcomment = AddComment()
            addcomment.text = request.POST['addcomment']
            addcomment.create_data = timezone.datetime.now()
            addcomment.save()
        
        return redirect('detail')

    else:
        comment_list = Comment.objects.all()
        addcomment_list = AddComment.objects.all()

        return render(request, 'detail.html',{
            'comment_list' : comment_list,
            'addcomment_list' : addcomment_list
        })
