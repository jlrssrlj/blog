from blogs.models import Categorias


def get_categories(_):
    categories = Categorias.objects.all()
    return {"categories": categories}
