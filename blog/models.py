from django.db import models
from django.contrib.auth.models import User

class BlogPost_table(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()