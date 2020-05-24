from django.shortcuts import render, redirect, get_object_or_404
from idea.models import Idea_Comments, Idea_AddComments, Idea
from signIn.models import Idea_Cart
from django.utils import timezone
from signIn.models import Profile

def detail(request, detail_id):
    
    if request.method == 'POST':

        comment = request.POST.get('comment', 0)
        addcomment = request.POST.get('addcomment', 0)
        cart = request.POST.get('cart', 0)

        if 'comment' in request.POST:
            comment = Idea_Comments()
            comment.user = request.user
            comment.text = request.POST['comment']
            comment.create_data = timezone.datetime.now()
            comment.save()

        elif 'addcomment' in request.POST:
            addcomment = Idea_AddComments()
            addcomment.user = request.user
            addcomment.text = request.POST['addcomment']
            addcomment.create_data = timezone.datetime.now()
            addcomment.save()

        elif 'cart' in request.POST:
            current_user = request.user
            current_user_profile = Profile.objects.get(email = current_user.email)
            current_idea = Idea.objects.get(pk = detail_id)
            current_user_cart = Idea_Cart.objects.all().filter(user = current_user, idea = current_idea)
            
            if current_user_cart:
                cart = Idea_Cart.objects.get(user = current_user, idea = current_idea)
                if cart.add_cart == True:
                    cart.add_cart = False
                    cart.save()
                elif cart.add_cart == False:
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
        # pk에 해당하는 아이디어 
        idea_detail = get_object_or_404(Idea, pk = detail_id)
        user = idea_detail.user
        user_profile =  get_object_or_404(Profile, user = user) # 어떻게 봐볼깝?
        full_hash_tag = idea_detail.idea_hashtag 
        hash_tag = full_hash_tag.replace(',','').split()
        user = idea_detail.user
        idea_id = idea_detail.id
        user_profile =  Profile.objects.get(email = user.email)


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

        # user permission (현재 로그인한 유저)
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
            'hash_tag':hash_tag,
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
            'user': user,
            'current_user_cart_add' : current_user_cart_add,
        })
        else :
            return render(request, 'detail.html',{
            'comment_list' : comment_list,
            'comments_count' : comments_count,
            'addcomment_list_all' : addcomment_list_all,
            'detail':idea_detail,
            'hasg_tag':hash_tag,
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
            'user': user,
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
