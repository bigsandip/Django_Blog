from django.shortcuts import render
from blog.models import Post
# we can use from .models import Post also
# from django.http import HttpResponse

# Create your views here.


post = [
    {
        'title': 'Title1',
        'author': 'Sandip',
        'content': 'content1',
        'date': '17th Dec 2019'
    },
    {
        'title': 'Title2',
        'author': 'Mishra',
        'content': 'content2',
        'date': '20th Dec 2019'

    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
