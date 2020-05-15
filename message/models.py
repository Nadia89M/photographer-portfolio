from django.db import models
from datetime import datetime

# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
