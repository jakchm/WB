from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=26)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=26)
    category = models.ForeignKey(Category, related_name='main_category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name 