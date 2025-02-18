from django.shortcuts import redirect, render
from blogs.models import Blog, Categorias
from .forms import RegistrationForm


def home(request):
    
    posts = Blog.objects.filter(is_featured = True).order_by('update_at')
    context = {        
        'featured_posts': posts
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    return render(request, 'login.html')