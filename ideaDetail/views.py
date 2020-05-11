from django.shortcuts import render, redirect, get_object_or_404
from idea.models import Idea_Comments, Idea_AddComments, Idea
from django.utils import timezone
from signIn.models import Profile

def detail(request, detail_id):
    
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

        idea_detail = get_object_or_404(Idea, pk = detail_id)
        user = idea_detail.user
        user_profile =  Profile.objects.get(user = user)
        full_hash_tag = idea_detail.idea_hashtag
        hash_tag = full_hash_tag.replace(',','').split()
        

        return render(request, 'detail.html',{
            'comment_list' : comment_list,
            'addcomment_list' : addcomment_list,
            'detail':idea_detail,
            'hasg_tag':hash_tag,
            'user_profile' : user_profile,
        })

def delete(request, detail_id):
    idea_detail = get_object_or_404(Idea, pk = detail_id)
    idea_detail.delete()
    return redirect('idea')

def edit(request, detail_id):
    idea_detail = get_object_or_404(Idea, pk = detail_id)

    if request.method == 'POST':
        idea_detail.idea_title = request.POST['IdeaName']
        idea_detail.idea_subtitle = request.POST['IdeaSubtitle']
        idea_detail.idea_description = request.POST['IdeaContent']
        #idea_detail.idea_image
        idea_detail.idea_hashtag = request.POST['IdeaHashTag']
        idea_detail.save()
        return redirect('/detail/' + str(detail_id))
    else:
        return render(request, 'submit.html', {'idea_detail':idea_detail})
