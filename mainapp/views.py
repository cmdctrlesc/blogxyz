from django.shortcuts import render
from .models import BlogPost


def home(request):
    posts = BlogPost.objects.all()

    return render(request, 'home.html', context={'posts': posts})


def about(request):
    return render(request, 'about.html')


def post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    title = post.title
    subtitle = post.subtitle
    content = post.content
    context = {'title': title, 'subtitle': subtitle, 'content': content}
    return render(request, 'post.html', context)
