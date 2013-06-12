from django.http import HttpResponse
from django.shortcuts import render
from django_mongokit import get_database

def index(request):
    coll = get_database()['blogposts']
    posts = coll.BlogPost.find()
    return render(request, 'blog/post_list.html', {'posts': posts}) 

def blog_post(request, slug):
    return HttpResponse('blog slug = {0}'.format(slug))
