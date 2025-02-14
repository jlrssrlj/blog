from django.shortcuts import render

from blogs.models import Blog, Categorias


def home(request):
    
    posts = Blog.objects.filter(is_featured = True).order_by('update_at')
    context = {        
        'featured_posts': posts
    }
    return render(request, 'home.html', context)