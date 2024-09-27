from rest_framework import viewsets, status
from rest_framework.response import Response
from performer.models import Artist, Band, Performer
from performer.serializers import PerformerSerializer, ArtistSerializer, BandSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class PerformerViewSet(viewsets.ViewSet):


    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'genres']


    def list(self, request):
        artists = Artist.objects.all()
        bands = Band.objects.all()

        # Combine both querysets into a single list
        performers = list(artists) + list(bands)

        # Sort performers by name or another field if needed
        performers.sort(key=lambda x: x.name)

        # Serialize the combined list
        serializer = PerformerSerializer(performers, many=True)

        return Response(serializer.data)

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    # def create(self, request, *args, **kwargs):
        
    #     serializer = self.get_serializer(data=request.data, many=True)  # Enable many=True for bulk
    #     serializer.is_valid(raise_exception=True)
    #     bands = serializer.save()
    #     return Response(ArtistSerializer(bands, many=True).data, status=status.HTTP_201_CREATED)

class BandViewSet(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

    def create(self, request, *args, **kwargs):
        
        # if not isinstance(request.data, list):
        #     return Response({"detail": "Expected a list of items."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data, many=True)  # Enable many=True for bulk
        serializer.is_valid(raise_exception=True)
        bands = serializer.save()
        return Response(BandSerializer(bands, many=True).data, status=status.HTTP_201_CREATED)