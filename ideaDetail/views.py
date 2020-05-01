from django.shortcuts import render, redirect
from ideaDetail.models import Comment
from django.utils import timezone

def detail(request):
    
    if request.method == 'POST':
        comment = Comment()
        comment.text = request.POST['comment']
        comment.create_data = timezone.datetime.now()
        comment.save()

        return redirect('detail')

    else:
        comment_list = Comment.objects.all()

    return render(request, 'detail.html',{'comment_list' : comment_list})
