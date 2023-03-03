from django.db import models

class Fish(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Sculptures(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Channels(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Plants(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Other(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title