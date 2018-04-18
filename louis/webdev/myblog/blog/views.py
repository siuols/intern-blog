from django.shortcuts import render

from django.views import View

from .models import Index, Post

# Create your views here.

class IndexView(View):
    def get(self, request, pk, *args, **kwargs):
        index = Index.objects.filter(pk=pk).order_by('-date_created')
        context = {
            'index': index,
        }
        return render(request, "blog/index.html", context)

class PostView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.filter(id=post_id).order_by('-date_created')
        context = {
            'object_list': post,
        }
        return render(request, "blog/post_list.html", context)