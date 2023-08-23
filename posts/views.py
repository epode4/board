from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)

def detail(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'detail.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # post = Post()s

    post = Post(title=title, content=content)
    post.save()

    return redirect('posts:detail', id=post.id)

def delete(requesets, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('posts:index')
