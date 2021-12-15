from django.shortcuts import render, redirect
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

def post(request, pk):
    post = Post.objects.get(id=pk)
    post_messages = post.message_set.all().order_by('-created')
    

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('body')
        )
        post.participants.add(request.user)
        return redirect('room', pk=post.id)

    context = {'post': post, 'post_messages': post_messages}

    return render(request, 'base/post.html', context)
