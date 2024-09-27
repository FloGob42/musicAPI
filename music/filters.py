from django.contrib.contenttypes.models import ContentType
from django_filters import rest_framework as filters
from .models import Music

class MusicFilter(filters.FilterSet):
    performer = filters.CharFilter(method='filter_performer')

    class Meta:
        model = Music
        fields = ['genre', 'performer']

    def filter_performer(self, queryset, name, value):
        """
        Filter the queryset based on performer type and name.
        Expected format for `value`: 'artist:John Doe' or 'band:Led Zeppelin'.
        """
        try:
            performer_type, performer_name = value.split(':')
            # Determine the appropriate content type based on the performer type
            content_type = ContentType.objects.get(model=performer_type)

            # Use `performer__name` for `Band` and a concatenated `first_name` and `name` for `Artist`
            if performer_type.lower() == 'band':
                # If performer is a band, filter by the band name
                return queryset.filter(content_type=content_type, performer__name=performer_name)
            elif performer_type.lower() == 'artist':
                # If performer is an artist, split into first and last name
                first_name, last_name = performer_name.split(' ', 1)
                return queryset.filter(content_type=content_type, performer__first_name=first_name, performer__name=last_name)
        except (ValueError, ContentType.DoesNotExist):
            # Return the unfiltered queryset if the input format is invalid or content type not found
            return queryset.none()
        
        