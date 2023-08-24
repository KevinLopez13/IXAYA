from django.db import models

# Create your models here.


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=60, null=True)
    content = models.TextField(max_length=3000, null=True)
    author = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='img/', blank=True, null=True)


class Patrocinador(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=200)