from django.urls import path
from .import views


app_name = 'record'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('trackwoman', views.IndextrackwomanView.as_view(), name='trackwoman'),
    path('roadman', views.IndexroadmanView.as_view(), name='roadman'),
    path('worldtrackman',views.IndextrackworldmanView.as_view(), name='worldindex'),
    path('roadwoman',views.IndexroadwomanView.as_view(), name='roadwoman'),
]