from django.urls import path

from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.PostView1.as_view(), name='index'),

]