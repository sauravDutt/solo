from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Message, Post, Topic

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    posts = Post.objects.filter(
        Q(topic__name__icontains= q) |
        Q(title__icontains=q) |
        Q(discription__icontains=q)
        )

    topics = Topic.objects.all()
    post_count = posts.count()
    post_messages = Message.objects.all()

    context = {'posts': posts, 'topics': topics, 'post_count': post_count, 'post_messages': post_messages}
    return render(request, 'base/home.html', context)

