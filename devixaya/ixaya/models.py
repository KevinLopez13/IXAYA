from django.db import models

# Create your models here.


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=60, null=True)
    content = models.TextField(max_length=3000, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    link = models.CharField(max_length=500, null=True, blank=True)


class Patrocinador(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='sponsors/', blank=True, null=True)

class CarruselItem(models.Model):
    image = models.ImageField(upload_to='carrusel/')