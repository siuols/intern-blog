from django.db import models

# Create your models here
class blog(models.Model):
    Heading = models.CharField(max_length=150)
    Sub_Heading = models.CharField(max_length=150)



class     