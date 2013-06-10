from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url( r'^(?P<slug>[\w-]+)/$', views.blog_post, name="blog_post")
)
