from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Profile, Idea_Cart
from idea.models import Idea, Idea_Comments, Idea_AddComments

def mypage(request):
    if request.user.is_authenticated == True:
        profile = get_object_or_404(Profile.objects.all().filter(email = request.user.email))
        myidea = Idea_Cart.objects.all().filter(user = request.user)
        comment = Idea_Comments.objects.all().filter(user = request.user).count()
        add_comment = Idea_AddComments.objects.all().filter(user = request.user).count()
        comment_all = comment + add_comment
        cart = Idea_Cart.objects.all().filter(user = request.user)
        cart_all = Idea_Cart.objects.all().filter(user = request.user).count()
        return render(request, 'mypage.html', 
            {'profile' : profile, 
            'myidea' : myidea, 
            'comment_all' : comment_all, 
            'cart_all' : cart_all,
            'cart' : cart}
        )
    else:
        
        return render(request, 'signIn.html')

def edit(request):
    return render(request, 'mypageedit.html')

def comments(request):
    comment = Idea_Comments.objects.all().filter(user = request.user)
    add_comment = Idea_AddComments.objects.all().filter(user = request.user)
    comments = comment.union(add_comment)
    return render(request, 'comments.html', {'comments':comments})