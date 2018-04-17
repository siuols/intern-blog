from django.db import models

# Create your models here

class blog(models.Model):
    Heading = models.CharField(max_length=150)
    Sub_Heading = models.CharField(max_length=150)
    
    def __str__(self):
        return '{}'.format(self.Heading)

class post(models.Model):
    Title = models.CharField(max_length=150)
    Sub_Title = models.CharField(max_length=150)
    Banner_Photo = models.ImageField(upload_to = 'static/media')
    Body = models.TextField()
    Author = models.CharField(max_length=150)
    Date = models.DateTimeField(auto_now_add=True)
    Date_modified = models.DateTimeField(auto_now_add=True)
    Blog = models.ForeignKey(blog, on_delete=models.CASCADE) 
    Category = models.ForeignKey('category', on_delete=models.CASCADE)
    Tags = models.ForeignKey('tags', on_delete=models.CASCADE)
    status = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
        ('Hidden', 'Hidden'),
    )
    Status            = models.CharField(max_length=6, choices=status, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.Title)


class category(models.Model):
    category_title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.category_title)

class tags(models.Model):
    tags_title = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.tags_title)