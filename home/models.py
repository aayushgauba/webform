from django.db import models

class Chain(models.Model):
    birdType = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    activeVolunteer = models.BooleanField()
    contact = models.CharField(max_length = 100)
    comments = models.TextField()
    