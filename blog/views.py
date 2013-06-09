from django.http import HttpResponse

def index(request):
    return HttpResponse('blog index')

def blog_post(request, id):
    return HttpResponse('blog id = {0}'.format(id))
