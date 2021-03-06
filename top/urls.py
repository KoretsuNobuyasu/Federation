from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'top'

urlpatterns = [
    path('', views.TopViews.as_view(),name='top'),
    path('top', views.IndexViews.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
