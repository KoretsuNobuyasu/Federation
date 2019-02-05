from django.views import generic
from .models import Gamesinformation, Category
from django.shortcuts import get_object_or_404

class IndexView(generic.ListView):
    model = Gamesinformation
    paginate_by = 10

    def get_queryset(self):
        return Gamesinformation.objects.order_by('-created_at')


class CategoryView(generic.ListView):
    model = Gamesinformation
    paginate_by = 10

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Gamesinformation.objects.order_by('-created_at').filter(category=category)
        return queryset


class DetailView(generic.DetailView):
    model = Gamesinformation