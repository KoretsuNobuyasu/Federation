from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Topics
 
class IndexViews(generic.ListView):
    model = Topics

    def get_queryset(self):
        return Topics.objects.order_by('-created_at')