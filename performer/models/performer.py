from django.db import models
from music.models import Music
from album.models import Album

# Create your models here.

class Performer(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    musics = models.ManyToManyField(Music, related_name='musics', blank= True)
    albums= models.ManyToManyField(Album, related_name='musics', blank=True)
    class Meta:
        abstract = True  



