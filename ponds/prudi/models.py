from django.db import models

class Fish(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

class Sculptures(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

class Channels(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

class Plants(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

class Other(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)