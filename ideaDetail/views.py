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
        
        return redirect('/detail/'+ str(detail_id))

    else:
        # pk에 해당하는 아이디어 
        idea_detail = get_object_or_404(Idea, pk = detail_id)
        
        # 아이디어 해시태그, 작성자, 순번, 프로필
        full_hash_tag = idea_detail.idea_hashtag
        hash_tag = full_hash_tag.replace(',','').split()
        user = idea_detail.user
        user_school = idea_detail.user.user_school
        idea_id = idea_detail.id
        user_profile =  idea_detail.user.user_image

        # 아이디어에 해당하는 댓글 가져오기
        comment_list_all = Idea_Comments.objects.all()
        comment_list = comment_list_all.filter(idea = idea_id) # 아이디어 순번에 맞는 댓글들
        comment_num = comment_list.count()
        comment_check = []

        # 댓글에 해당하는 대댓글 가져오기 위해 댓글들에 pk 부여하기
        comments = {}   # 댓글 pk 부여
        i = 0        
        for comment in comment_list:
            comments[i] = comment.id
            comment_check.append(comment.id)
            i += 1

            if (i == comment_num):
                break

        comments_count = len(comments)

        # 대댓글 전부 가져오기
        addcomment_list_all = Idea_AddComments.objects.all()
        
        # 아이디어에 해당하는 대댓글들을 각 댓글에 부여해줘야 함

        add_comments = {} # 댓글 순번에 따른 대댓글 부여
        add_comments_num = {}
        value = [] # 순번에 해당하는 댓글의 대댓글들

        for k in range(comments_count): 

            # pk에 해당하는 댓글의 대댓글들 쿼리 가져오기
            add_comments[comments[k]] = addcomment_list_all.filter(idea_comments = comments[k])
            add_comments_num[comments[k]] = len(add_comments[comments[k]])   # k번째 댓글의 대댓글 개수 리스트에 추가

        # 댓글 수만큼 value 리스트에 순번에 해당하는 대댓글들 넣기
        for t in range(comments_count):

            value.append(add_comments[comments[t]])

        return render(request, 'detail.html',{
            'comment_list' : comment_list,
            'comments_count' : comments_count,
            'addcomment_list_all' : addcomment_list_all,
            'detail':idea_detail,
            'hash_tag':hash_tag,
            'user_profile' : user_profile,
            'comment_num' : comment_num,
            'add_comments_num' : add_comments_num,
            'comments' : comments,
            'add_comments' : add_comments,
            'value' : value,
            'comment_check' : comment_check,
            'user' : user,
            'user_school': user_school,
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
