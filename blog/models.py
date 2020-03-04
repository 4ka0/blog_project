from django.db import models
from django.urls import reverse


class Post(models.Model):
    ''' 
    Class representing a single blog post.
    
    For the author we're using a ForeignKey field as this allows for 
    a many-to-one relationship, meaning that the author can be the author
    of many blog posts.
    
    The User model is referenced to make authentication possible.
    
    Many-to-one relationships require an on_delete option. Here CASCADE is
    used, meaning that when the referenced object is deleted, associated 
    objects are also deleted (i.e. when you remove a blog post, the associated 
    comments are also deleted).
    '''

    title = models.CharField(max_length=200)
    body = models.TextField()
    
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
