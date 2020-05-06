<<<<<<< HEAD
from django.shortcuts import render

def detail(request):
    return render(request, 'detail.html')
=======
from django.shortcuts import render, get_object_or_404, redirect
from idea.models import Idea

def detail(request, detail_id):
    idea_detail = get_object_or_404(Idea, pk = detail_id)
    full_hash_tag = idea_detail.idea_hashtag
    hash_tag = full_hash_tag.split()
    return render(request, 'detail.html', {'detail':idea_detail, 'hasg_tag':hash_tag})

def delete(request, detail_id):
    idea_detail = get_object_or_404(Idea, pk = detail_id)
    idea_detail.delete()
    return redirect('idea')
>>>>>>> idea & detail 연결 및 수정
