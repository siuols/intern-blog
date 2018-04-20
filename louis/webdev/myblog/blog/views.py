from django.shortcuts import render, Http404, get_object_or_404, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponseRedirect

from django.views import View

from django.contrib.auth.models import User

from .forms import CommentForm

from .models import Index, Post, Comment

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        index = Index.objects.all()
        context = {
            'index': index,
        }
        return render(request, "home.html", context)

class IndexView(View):
    def get(self, request, pk, *args, **kwargs):
      # index = Index.objects.get(pk=pk)
      index = get_object_or_404(Index, pk=pk)
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
      post = get_object_or_404(Post, pk=post_id, status='published')
      comment = post.comment_set.all()
      context = {
          'post': post,
          'comment': comment,
        }
      return render(request, "blog/post_list.html", context)

def comment_new(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/comment.html', context)
