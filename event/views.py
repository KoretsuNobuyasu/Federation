from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    model = Post

class DetailView(generic.DetailView):
    model = Post