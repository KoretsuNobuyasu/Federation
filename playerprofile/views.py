from django.views import generic
from .models import Profile

class IndexView(generic.ListView):
    model = Profile

    def get_queryset(self):
        return Profile.objects.order_by('birth')

class DetailView(generic.DetailView):
    model = Profile