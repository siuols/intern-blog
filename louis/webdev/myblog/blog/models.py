from django.conf import settings

from django.core.paginator import Paginator

from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.

class Index(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    heading                 = models.CharField(max_length=120)
    sub_heading             = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.heading)

class Tag(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    tag                     = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.tag)

class Category(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    category                = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.category)


STATUS_CHOICES = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden')
)

# class PostManager(models.Manager):
#     def post(self, index_obj):
#         if index_obj.index:
#             og_parent = index_obj.index
#         else:
#             og_parent = index_obj

#         qs = self.get_queryset().filter(index=og_parent)

#         if qs.exits():
#             return None

#         obj = self.model(
#                 index = og_parent,
#                 user = user,
#                 post_id = index_obj.index,
#             )
#         obj.save()
#         return obj

class Post(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    index                   = models.ForeignKey('Index', on_delete=models.CASCADE,)
    title                   = models.CharField(max_length=120)
    subtitle_or_caption     = models.CharField(max_length=120)
    banner_photo            = models.ImageField()
    author                  = models.CharField(max_length=120)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    tags                    = models.ManyToManyField(Tag)
    category                = models.ForeignKey('Category', on_delete=models.CASCADE,)
    body                    = models.TextField(max_length=1000)
    status                  = models.CharField(max_length=9, choices=STATUS_CHOICES, default='published',)

    # objects                 = PostManager()

    def __str__(self):
        return '{}'.format(self.index)

    def get_parent(self):
        the_parent = self
        if self.index:
            the_parent = self.index
        return the_parent

    def get_child(self):
        index = self.get_parent()
        qs = Post.objects.filter(index=index)
        qs_parent = Post.objects.filter(pk=index.pk)
        return (qs | qs_parent)
