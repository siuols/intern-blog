from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import View

from .models import Index, Post

# Create your views here.

# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25)

#     page = request.GET.get('page')
#     Contact = paginator.get_page(page)
#     return render(request, 'list.html', {'contact': contacts})


class IndexView(View):
  def get(self, request, pk, *args, **kwargs):
    index = Index.objects.filter(pk=pk).order_by('-date_created')

    post_list = Post.objects.all()

    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    post = paginator.get_page(page)

    context = {
            'index': index,
            'post': post,
      }
    return render(request, "blog/index.html", context)

class PostView(View):
  def get(self, request, post_id, *args, **kwargs):
      post = Post.objects.filter(id=post_id).order_by('-date_created')
      context = {
          'object_list': post,
      }
      return render(request, "blog/post_list.html", context)
