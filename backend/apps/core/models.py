from django.db import models
from apps.category.models import Category, SubCategory
from PIL import Image
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=5000)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='subcategory', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    views = models.IntegerField(default=0)
    allow_comment = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title