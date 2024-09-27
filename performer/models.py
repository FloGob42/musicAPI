from django.db import models

class Performer(models.Model):
    name = models.CharField(max_length=100)
    genres = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    
    class Meta:
        abstract = False

class Artist(Performer):
    first_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.name}"
    
class Band(Performer):
    formation_year = models.PositiveIntegerField(null=True, blank=True)
    

    def __str__(self):
        return self.name