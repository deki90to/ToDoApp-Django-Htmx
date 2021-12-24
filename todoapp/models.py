from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.post}'
    
    class Meta:
        ordering = ['-created']

