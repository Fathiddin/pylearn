from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class UploadFile(models.Model):
    name = models.CharField(max_length=100)
    images = models.FileField(upload_to='files/')

    def __str__(self):
        return str(self.name)


class Posts(models.Model):
    title = models.CharField(max_length=150)
    slug_id = models.SlugField(unique=True)
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)