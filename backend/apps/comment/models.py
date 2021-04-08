from django.db import models
from apps.core.models import Post

# Create your models here.

class Comment(models.Model):
    comment = models.TextField(max_length=256)
    advert = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment[:20]