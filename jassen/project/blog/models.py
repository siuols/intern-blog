from django.db import models
from django.conf import settings
from django.urls import reverse 
User = settings.AUTH_USER_MODEL

# Create your models here
POST_STATUS = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden'),
)

class Index(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=150)
    
    def __str__(self):
        return '{}'.format(self.heading)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    sub_Title = models.CharField(max_length=150)
    banner_photo = models.ImageField(upload_to = 'static/media')
    body = models.TextField()
    author = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Index, on_delete=models.CASCADE) 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("tags",related_name="Tags")
    status = models.CharField(max_length=9, choices=POST_STATUS, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.title)

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.title)

class Tags(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.title)