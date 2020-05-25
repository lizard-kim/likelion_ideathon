from django.shortcuts import render, redirect, get_object_or_404
from idea.models import Idea_Comments, Idea_AddComments, Idea, Idea_image_storage
from accounts.models import Idea_Cart, Profile
from django.utils import timezone

def detail(request, detail_id):
    if request.method == 'POST':
        comment = request.POST.get('comment', 0)
        addcomment = request.POST.get('addcomment', 0)
        cart = request.POST.get('cart', 0)

        if 'comment' in request.POST:
            comment = Idea_Comments()
            comment.user = request.user
            comment.idea = Idea.objects.get(pk = detail_id)
            comment.text = request.POST['comment']
            comment.create_data = timezone.datetime.now()
            comment.save()

        elif 'cart' in request.POST:
            current_user = request.user #로그인한 유저
            current_user_profile = Profile.objects.get(email = current_user.email) #로그인한 유저 프로필
            current_idea = Idea.objects.get(pk = detail_id) #지금 내가 위치해 있는 페이지 아이디어내용
            current_user_cart = Idea_Cart.objects.all().filter(user = current_user, idea = current_idea)
            
            if current_user_cart:
                cart = Idea_Cart.objects.get(user = current_user, idea = current_idea)
                if cart.add_cart:
                    cart.add_cart = False
                    cart.save()
                else:
                    cart.add_cart = True
                    cart.save()
            else:
                user_cart = Idea_Cart()
                user_cart.user = current_user_profile
                user_cart.idea = current_idea
                user_cart.add_cart = True
                user_cart.save()


        return redirect('/detail/'+ str(detail_id))

    else:
        # pk 에 해당하는 아이디어 
        idea_detail = Idea.objects.get(pk = detail_id)
        user = idea_detail.user
        # full_hash_tag = idea_detail.idea_hashtag
        # hash_tag = full_hash_tag.replace(',','').split()
        idea_id = idea_detail.id
        idea_images = Idea_image_storage.objects.all().filter(idea = idea_detail)
        user_profile =  Profile.objects.get(email = user.email)
        is_logined_user = request.user.is_authenticated

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

        # 로그인한 유저가 있다면
        if request.user.is_authenticated :
            current_user = request.user
            current_user_profile = Profile.objects.get(email = current_user.email)

            # 현재 로그인한 유저가 해당 아이디어 가지고 있는지 체크
            current_user_cart = Idea_Cart.objects.all().filter(user = current_user, idea = idea_detail)
        
            if current_user_cart :  # 해당 아이디어에 대해 장바구니 가지고 있다면
                current_user_cart_add = Idea_Cart.objects.get(user = current_user, idea = idea_detail) # 겟또

                return render(request, 'detail.html',{
                    'comment_list' : comment_list,
                    'comments_count' : comments_count,
                    'addcomment_list_all' : addcomment_list_all,
                    'detail':idea_detail,
                    'comment_num' : comment_num,
                    'add_comments_num' : add_comments_num,
                    'comments' : comments,
                    'add_comments' : add_comments,
                    'value' : value,
                    'comment_check' : comment_check,
                    'idea_detail' : idea_detail,
                    'current_user' : current_user,  # 현재 로그인한 사람
                    'current_user_profile' : current_user_profile,
                    'user_profile' : user_profile,
                    'user': user,   # 아이디어 작성자 
                    'idea_images' : idea_images,
                    'current_user_cart_add' : current_user_cart_add,
                    'is_logined_user' : is_logined_user,  # 로그인 여부 확인 T/F
                })
            else :
                return render(request, 'detail.html',{
                    'comment_list' : comment_list,
                    'comments_count' : comments_count,
                    'addcomment_list_all' : addcomment_list_all,
                    'detail':idea_detail,
                    # 'hasg_tag':hash_tag,
                    'user_profile' : user_profile,
                    'comment_num' : comment_num,
                    'add_comments_num' : add_comments_num,
                    'comments' : comments,
                    'add_comments' : add_comments,
                    'value' : value,
                    'comment_check' : comment_check,
                    'idea_detail' : idea_detail,
                    'current_user' : current_user,
                    'current_user_profile' : current_user_profile,
                    'user_profile' : user_profile,
                    'user': user,   # 아이디어 글 작성자
                    'idea_images' : idea_images,
                    'is_logined_user' : is_logined_user,    # 로그인 여부 확인 T/F
                }) 
        else:
            return render(request, 'detail.html',{
                    'comment_list' : comment_list,
                    'comments_count' : comments_count,
                    'addcomment_list_all' : addcomment_list_all,
                    'detail':idea_detail,
                    # 'hasg_tag':hash_tag,
                    'comment_num' : comment_num,
                    'add_comments_num' : add_comments_num,
                    'comments' : comments,
                    'add_comments' : add_comments,
                    'value' : value,
                    'comment_check' : comment_check,
                    'idea_images' : idea_images,
                    'user' : user,  # 아이디어 글 작성자
                    'idea_detail' : idea_detail,
                    'is_logined_user' : is_logined_user,    # 로그인 여부 확인 T/F
                }) 

def subcomment(request, detail_id, comment_id):
    if request.method == 'POST':
        text = request.POST['text']
        profile = get_object_or_404(Profile.objects.all().filter(email = request.user.email))
        comment = Idea_Comments.objects.filter(id=comment_id).get()

        newsubcomment = Idea_AddComments.objects.create(
            user = profile,
            text = text,
            idea_comments = comment,
        )

        return redirect('/detail/'+ str(detail_id))

# def comment_edit(request, detail_id, comment_id):
#     if request.method == 'POST':
#         text = request.POST['comment']
#         comment = Idea_Comments.objects.filter(id=comment_id).get()
#         comment.text = text
#         comment.save()
        
#         return redirect('/detail/'+ str(detail_id))
#     else:
#         return render(request, 'detail.html' , {'comment' : comment})


def delete(request, detail_id):
    idea_detail = get_object_or_404(Idea, pk = detail_id)
    idea_detail.delete()
    return redirect('idea')

def edit(request, detail_id):
    idea_detail = Idea.objects.get(pk = detail_id)

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

# def comment_edit(request, comment_id, detail_id):
#     idea_comment = Idea_Comments.objects.get(pk = comment_id)

#     if request.method == 'POST':
#         idea_comment.text = request.POST['comment']
#         idea_comment.save()
#         return redirect('/detail/' + str(detail_id))
#     else:
#         return render(request, 'detail.html', {'idea_comment': idea_comment})

def comment_delete(request, comment_id, detail_id):
    idea_comment = Idea_Comments.objects.get(pk = comment_id)
    idea_comment.delete()
    return redirect('/detail/'+ str(detail_id))

def addcomment_delete(request, addcomment_id, detail_id):
    idea_addcomment = Idea_AddComments.objects.get(pk = addcomment_id)
    idea_addcomment.delete()
    return redirect('/detail/'+ str(detail_id))
