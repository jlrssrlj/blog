from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Categorias
from dashboards.forms import CategoryForm

# Create your views here.
def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html',context)

def edit_category(request, pk):
    category = get_object_or_404(Categorias, pk=pk)
    if request.method=='POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_Category.html', context)

def delete_category(request,pk):
    category = get_object_or_404(Categorias, pk=pk)
    category.delete()
    return redirect('categories')