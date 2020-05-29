from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from accounts.models import Profile, Idea_Cart
from django.contrib import auth
from idea.models import Idea, Idea_Comments, Idea_AddComments, Idea_image_storage
from django.contrib.auth.hashers import check_password
from accounts.forms import *

def mypage(request):
    if request.user.is_authenticated == True:
        profile = get_object_or_404(Profile.objects.filter(email = request.user.email))
        myidea = Idea.objects.filter(user = request.user)
        kk = Idea_image_storage.objects.filter(idea = myidea)
        comment = Idea_Comments.objects.filter(user = request.user).count()
        add_comment = Idea_AddComments.objects.filter(user = request.user).count()
        comment_all = comment + add_comment
        form = UserChangeForm()
        cart = Idea_Cart.objects.filter(user = request.user) #카트유저가 지금 로그인한 유저와 같아
        #cart_all = Idea_Cart.objects.all().exclude(user = request.user).count()
        cart_all = Idea_Cart.objects.filter( user = request.user, add_cart = True ).count()

        return render(request, 'mypage.html', 
            {'profile' : profile, 
            'myidea' : myidea, 
            'comment_all' : comment_all, 
            'cart_all' : cart_all,
            'cart' : cart,
            'form' : form,
            'kk':kk,
            }
        )
    else:
        return render(request, 'signIn.html')

def mypage_edit(request):
    if request.user.is_authenticated == True and request.method == 'POST':
        profile = Profile(email = request.user.email)
        #profile = Profile.objects.get(email = request.user.email)
        name = request.POST['name']
        password = request.POST['password']
        new_password = request.POST['new_password']
        password_confirm = request.POST['password_confirm']
        user_info = request.POST['user_info']
        user = request.user

        if check_password(password,user.password) and new_password == password_confirm:
            user.set_password(new_password)
            user.user_name = name
            user.user_about = user_info
            user.save()     
            
            auth.login(request, user)
            return redirect('../')
    return render(request, 'mypage.html')
def comments(request):
    comment = Idea_Comments.objects.all().filter(user = request.user)
    add_comment = Idea_AddComments.objects.all().filter(user = request.user)
    comments = comment.union(add_comment)
    return render(request, 'comments.html', {'comments':comments})