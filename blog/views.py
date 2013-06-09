from django.http import HttpResponse

def index(request):
    return HttpResponse('blog index')

def blog_post(request, slug):
    return HttpResponse('blog slug = {0}'.format(slug))
