import math
from django.shortcuts import render
from .models import Idea
from idea.models import Idea_image_storage, Idea_Comments
from accounts.models import Profile
from django.core.paginator import Paginator
from django.core.cache import cache

def idea(request):
    ideas = Idea.objects.all().order_by('-id')
    count = ideas.count()
    return render(request, 'idea.html', 
        {'ideas':ideas, 
        'count' : count,
        })
