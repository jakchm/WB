from django.db import models
from apps.core.models import Post

# Create your models here.

class Ratings(models.Model):
    rate = models.IntegerField(default=2)
    advert = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Ratings"
