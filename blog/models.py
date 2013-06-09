import datetime

from mongokit import *
from django_mongokit import connection
from django_mongokit.document import DjangoDocument
from django.template.defaultfilters import slugify

class BlogPost(DjangoDocument):
    class Meta:
        verbose_name_plural = 'BlogPosts'

    structure = {
        'title': unicode,
        'content': unicode,
        'author': unicode,
        'published_date': datetime.datetime,
        'slug': unicode
    }

    required_fields = [ 'title', 'content', 'author', 'published_date']

    default_values = {
        'published_date': datetime.datetime.utcnow,
    }

    use_dot_notation = True

    indexes = [
        { 'fields': ['published_date'] }        
    ] 

    def save(self, *args, **kwargs):
        if not self.get('slug'):
            self['slug'] = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

connection.register([BlogPost])
