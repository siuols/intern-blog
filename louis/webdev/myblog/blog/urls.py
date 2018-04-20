from django.urls import path

from . import views

from .views import IndexView, PostView, Home

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', IndexView.as_view(), name='index'),
    path('post/<int:post_id>/', PostView.as_view(), name='post-list'),
    path('post/comment/', views.comment_new, name='post-comment'),
    path('', Home.as_view(), name='home')
]
