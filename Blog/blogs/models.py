from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,models.CASCADE,related_name='posts')
    
    def __str__(self):
        return self.title
        return self.text