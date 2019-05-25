from django.db import models
from datetime import datetime

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    testimonial = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
