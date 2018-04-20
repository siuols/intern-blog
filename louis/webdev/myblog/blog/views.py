from django.shortcuts import render, Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import View

from django.contrib.auth.models import User

from .models import Index, Post

# Create your views here.

class IndexView(View):
  def get(self, request, pk, *args, **kwargs):
    index = Index.objects.get(pk=pk)

    post_list = index.post_set.filter(status='published')


    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
      post = paginator.page(page)
    except PageNotAnInteger:
      post = paginator.page(1)
    except EmptyPage:
      post = paginator.page(paginator.num_pages)

    context = {
        'index': index,
        'post': post,
      }
    return render(request, "blog/index.html", context)

class PostView(View):
  def get(self, request, post_id, *args, **kwargs):
    post = Post.objects.all()

    try:
      post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
      raise Http404("Post does not exist")

    context = {
        'post': post,
      }
    return render(request, "blog/post_list.html", context)
