from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here
POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden'),
)

class Blog(models.Model):
    heading = models.CharField(max_length=150)
    sub_Heading = models.CharField(max_length=150)
    
    def __str__(self):
        return '{}'.format(self.Heading)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    sub_Title = models.CharField(max_length=150)
    banner_Photo = models.ImageField(upload_to = 'static/media')
    body = models.TextField()
    author = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Post",related_name="Tags")
    Status = models.CharField(max_length=6, choices=POST_STATUS, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.Title)


class Category(models.Model):
    category_title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.category)

class Tags(models.Model):
    tags_title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.tags_title)