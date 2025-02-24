
from django import forms
from blogs.models import Categorias


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'