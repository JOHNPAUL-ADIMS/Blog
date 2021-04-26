from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey('auth.User', on_delete=CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    