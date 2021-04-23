from django.db import models

# Create your models here.

class ForbiddenUserNames(models.Model):
    name = models.CharField(max_length=36)


    def __str__(self):
        return self.name