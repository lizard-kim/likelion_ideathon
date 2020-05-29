import math
from django.shortcuts import render
from .models import Idea
from idea.models import Idea_image_storage
from accounts.models import Profile
from django.core.paginator import Paginator
from django.core.cache import cache

def idea(request):
    ideas = Idea.objects.all().order_by('?')
    count = ideas.count()
    profile = Profile.objects.all()
    paginator = Paginator(ideas,  12)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    page_range = 6
    return render(request, 'idea.html', {'ideas':ideas, 'posts':posts, 'profile' : profile, 'count' : count,})
