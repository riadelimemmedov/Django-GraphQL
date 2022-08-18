from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#!Author
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

#!Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author,related_name='posts',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.title)