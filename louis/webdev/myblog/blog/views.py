from django.shortcuts import render

from django.views import View

from .models import Index, Post

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        index = Index.objects.all().order_by('-date_created')
        context = {
            'object_list': index,
        }
        return render(request, "blog/index.html", context)

class PostView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all().order_by('-date_created')
        context = {
            'object_list': post,
        }
        return render(request, "blog/post_list.html", context)