from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=15, blank=True)
    content = models.TextField(max_length=1500)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.content