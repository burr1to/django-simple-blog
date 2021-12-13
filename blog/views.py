from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def home(request):
    
    #newmanager is a type of custom manager for a subset of a set that is models. newmanager only selects the object with blog_status that is published.
    
    all_posts = Post.newmanager.all()
    published = Post.objects.filter(blog_status = 'published')
    
   
    
    show = {
        'all_posts' : all_posts,
        'published':published,
        
    }
    
    return render(request,'index.html',show)

#here, it takes request and post. the post value is given as the slug
def post_single(request, post):
    #query is made, the Post with the given slug is stored in 'post', plus only with blog_status which is published blog
    post = get_object_or_404(Post, blog_slug = post, blog_status = 'published')
    
    show2 =  {'post' : post}
    
    return render(request,'single.html', show2)
    
    
