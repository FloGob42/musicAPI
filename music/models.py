from django.db import models
from album.models import Album
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=200)
    length = models.DurationField(null=True, blank=True)
    albums = models.ManyToManyField(Album,related_name='musics', blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    interprete = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.titre