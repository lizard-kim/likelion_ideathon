from django.shortcuts import render, get_object_or_404, redirect
from idea.models import Idea

def detail(request, detail_id):
    idea_detail = get_object_or_404(Idea, pk = detail_id)
    full_hash_tag = idea_detail.idea_hashtag
    hash_tag = full_hash_tag.replace(',','').split()
    return render(request, 'detail.html', {'detail':idea_detail, 'hasg_tag':hash_tag})

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
