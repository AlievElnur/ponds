from django.db import models

class Ponds(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")

class Yolo(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")

class Hoods(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photo/")