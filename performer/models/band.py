from performer import *
from artist import Artist

class Band(Performer):
    formation_date = models.DateField(null=True, blank=True)
    members = models.ManyToManyField(Artist, related_name='band_members', blank=True)

    def __str__(self):
        return self.name