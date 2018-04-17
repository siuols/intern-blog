from django.shortcuts import render

from django.views import View

from .models import Index, Category, Post, Tag

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        index = Index.objects.all()#.order_by('-published_date')[5]
        context = {
            'object_list': index,
        }
        return render(request, "blog/index.html", context)

# class IndexView(View):
#     template_name = 'blog/index.html'
#     def get_queryset(self):
#         return Index.objects.all().order_by('-date_created')[:5]



# class IndexView(View):
#     template_name = 
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello, World!')