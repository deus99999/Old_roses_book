from django.db import models


# class Text(models.Model):
#     text = models.TextField()
#     photo = models.ImageField(upload_to='photos/')
#     date_created = models.DateTimeField(auto_now_add=True)

from ckeditor.fields import RichTextField


class Text(models.Model):
    text = RichTextField()
    photo = models.ImageField(upload_to='photos/')
    date_created = models.DateTimeField(auto_now_add=True)