from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tinyblog.views.home', name='home'),
    # url(r'^tinyblog/', include('tinyblog.foo.urls')),
    
    url(r'^$', 'tinyblog.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
)
