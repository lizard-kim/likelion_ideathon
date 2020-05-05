from django.shortcuts import render
from .models import Idea
from django.core.paginator import Paginator

def idea(request):
    ideas = Idea.objects.all()
    paginator = Paginator(ideas, 12)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'idea.html', {'ideas':ideas, 'posts':posts})