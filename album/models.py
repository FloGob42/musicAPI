from django.db import models
from music_API.performer.models.performer import Performer
from music.models import Music
# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE, related_name='albums')
    musics = models.ManyToManyField(Music, on_delete=models.SET_NULL)
    def __str__(self):
        return self.titre