from django.db import models

# Create your models here.

class Performer(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    
    class Meta:
        abstract = True  

class Artist(Performer):
    first_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bands = models.ManyToManyField('Band', related_name='artists', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.name}"
    
class Band(Performer):
    formation_date = models.DateField(null=True, blank=True)
    members = models.ManyToManyField('Artist', related_name='band_members', blank=True)

    def __str__(self):
        return self.name