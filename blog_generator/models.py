from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_title = models.CharField(max_length=300)
    youtube_link = models.URLField()
    generated_content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.youtube_title
    
class Product(models.Model):
    """Model definition for Product."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, null=True)
    url = models.URLField(null=True)

    