from django.urls import path

from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.PostView1.as_view(), name='index'),
    path('draft', views.PostView2.as_view(), name='draft'),
    path('hidden', views.PostView3.as_view(), name='hidden'),

]