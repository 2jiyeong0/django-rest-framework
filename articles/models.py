from distutils.text_file import TextFile
from turtle import update
from venv import create
from django.db import models
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    context = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)