from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from blogs.models import Blog, Categorias

@require_http_methods(["GET"])
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status = 'Published', category=category_id)
    try:
        category = Categorias.objects.get(pk=category_id)
    except Categorias.DoesNotExist:
        return redirect('home')
    
    context ={
        'posts' : posts,
        'category': category,
        
    }
    return render(request, 'posts_by_category.html',context)

@require_http_methods(["GET"])
def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug = slug)
    context = {
        'single_blog': single_blog
    }
    return render(request, 'blogs.html',context)

@require_http_methods(["GET"])
def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains= keyword)| Q(short_description__icontains=keyword) | Q(blog_body__icontains = keyword))
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)