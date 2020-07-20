from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)  
    thumb=models.ImageField(default='default.png',blank=True)  

    def __str__(self):
        return f"{self.title[:20]}... - {self.author}"

    def snippet(self):
        return self.content[:50]+"..."
