from django.urls import path

from . import views

from .views import IndexView, PostView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/', PostView.as_view(), name='post-list')
]