from django.shortcuts import render
from .models import BlogPost, Project


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

def projects(request):
    projects = Project.objects.all()

    return render(request, 'projects.html', context={'projects': reversed(projects)})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    title = project.title
    subtitle = project.subtitle
    content = project.content
    context = {'problem': title, 'solution': subtitle, 'content': content,}
    return render(request, 'project.html', context)


