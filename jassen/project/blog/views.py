from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)
from .models import Post,Category,Tags,Index 
# Create your views here.

class PostView1(generic.ListView):
    def get(self, request): 
        query = self.request.GET.get('q')
        students = Post.objects.filter(status__contains='published',)
        context = {'post':post,}
        return render(request, "Post_list.html", context)


class PostView2(generic.ListView):
    def get(self, request): 
        query = self.request.GET.get('q')
        students = Post.objects.filter(status__contains='draft',)
        context = {'post':post,}
        return render(request, "Post1_list.html", context)



class PostView3(generic.ListView):
    def get(self, request): 
        query = self.request.GET.get('q')
        students = Post.objects.filter(status__contains='hidden',)
        context = {'post':post,}
        return render(request, "Post2_list.html", context)


