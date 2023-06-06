from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    hls_file = models.CharField(max_length=200)