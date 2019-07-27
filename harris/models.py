from django.db import models
from colorfield.fields import ColorField

class Blog(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=15, blank=True)
    content = models.TextField(max_length=1500)
    timestamp = models.DateTimeField()
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.title