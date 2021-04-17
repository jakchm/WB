from django.db import models
from apps.core.models import Post
from django.conf import settings

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=256)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.text[:20]