from performer import *
from band import Band

class Artist(Performer):
    first_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bands = models.ManyToManyField(Band, related_name='artists', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.name}"