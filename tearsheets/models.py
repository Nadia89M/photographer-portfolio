from django.db import models
from datetime import datetime

# Create your models here.
class Tearsheet(models.Model):
    title = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    is_vertical = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
