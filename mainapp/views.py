from django.shortcuts import render
from .models import BlogPost


def posts(request):
    posts = BlogPost.objects.exclude(title__icontains='Problem')

    return render(request, 'posts.html', context={'posts': reversed(posts)})


def about(request):
    return render(request, 'about.html')


def post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    title = post.title
    subtitle = post.subtitle
    content = post.content
    context = {'title': title, 'subtitle': subtitle, 'content': content}
    return render(request, 'post.html', context)
