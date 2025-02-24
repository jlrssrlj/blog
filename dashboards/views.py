from django.shortcuts import redirect, render
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
    return render(request, 'dashboard/edit_Category.html')