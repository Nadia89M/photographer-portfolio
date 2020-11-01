from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime

# Create your models here.


class Welcome(models.Model):
    title = models.CharField(max_length=200)
    content_left = RichTextUploadingField(blank=True)
    content_right = RichTextUploadingField(blank=True)

    def __str__(self):
        return self.title
