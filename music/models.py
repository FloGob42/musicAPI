from django.db import models
from album.models import Album
from music_API.performer.models.performer import Performer

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=200)
    length = models.DurationField(null=True, blank=True)
    Performer = models.ManyToManyField(Performer, on_delete=models.CASCADE, related_name='musics')
    albums = models.ManyToManyField(Album, on_delete=models.SET_NULL ,related_name='musics', null=True, blank=True)

    def __str__(self):
        return self.titre