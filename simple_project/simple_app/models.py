from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='post_image')
    
    def __str__(self):
        return self.name.username
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Mypost(models.Model):
    title = models.CharField(max_length=50)
    post_body = models.TextField()
    posting_time = models.DateTimeField(default=timezone.now)
    image1 = models.ImageField(upload_to='post_image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title