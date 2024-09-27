from django.db import models
from album.models import Album
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=200)
    length = models.DurationField(null=True, blank=True)
    albums = models.ManyToManyField(Album,related_name='musics', blank=True)
    genre = models.CharField(max_length=100, null=True, blank= True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ['artist', 'band']})
    object_id = models.PositiveIntegerField()
    performer = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.title