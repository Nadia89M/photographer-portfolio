from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime

# Create your models here.
class Activity(models.Model):
    class Meta:
        verbose_name_plural = "activities"
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    content = RichTextUploadingField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
