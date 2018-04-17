from django.contrib import admin

from .models import Index, Tag, Category, Post

# Register your models here.

admin.site.register(Index)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)