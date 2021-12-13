from django.db import models

    
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    
    class NewManager(models.Manager):
      #this filters by default if needed for only published posts. more dynamic. easier to access. can directly call newmanager in view.
        def get_queryset(self):
            return super().get_queryset() .filter(blog_status = 'published')
        
    
    #options is the choices = option for blog_status, the dropdown menu almost
    options = (
        ('draft', 'Draft'),
        ('published','Published'),
    )
    
    blog_title = models.CharField(max_length=500)
    
    blog_date = models.DateTimeField(default=timezone.localtime)
    blog_slug = models.SlugField(max_length=250,unique_for_date='blog_date')
    blog_status = models.CharField(max_length=10,choices = options, default = "draft")
    blog_author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
    blog_content = models.TextField(default = " ")
    blog_status = models.CharField(max_length =10, choices=options,default = 'draft')
    objects = models.Manager()

    newmanager = NewManager()
    
    
    #an absolute url that takes the slugs for the single posts and links it to every page
    def get_absolute_url(self):
        return reverse('blog:post_single',args = [self.blog_slug])
    class Meta:
        ordering = ('-blog_date',)
        #default output ordering will be from the blog_date. if -, then from the latest time.
    
    def __str__(self):
        return '{}'.format(self.blog_title)
    
    #return the actual title instead of just Post.object in the admin section :)
    
    
    
    
        