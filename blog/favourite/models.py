from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from post.models import  Post

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete= models.CASCADE)
    content = models.CharField(max_length=120)
    
    def __str__(self):
        return self.user.username