from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ['artist', 'band']})
    object_id = models.PositiveIntegerField()
    interprete = GenericForeignKey('content_type', 'object_id')

    
    def __str__(self):
        return self.title