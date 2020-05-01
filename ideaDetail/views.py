from django.shortcuts import render, redirect
from ideaDetail.models import Comment, AddComment
from django.utils import timezone

def detail(request):
    
    if request.method == 'POST':
        if request.POST.get == 'comment':
            comment = Comment()
            comment.text = request.POST.get('comment', '')
            comment.create_data = timezone.datetime.now()
            comment.save()
        else :
            addcomment = AddComment()
            addcomment.text = request.POST.get('addcomment', '')
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
