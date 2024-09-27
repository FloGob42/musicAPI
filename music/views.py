from .models import Music
from .serializers import MusicSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import MusicFilter


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MusicFilter

    # def create(self, request, *args, **kwargs):
        
    #     # if not isinstance(request.data, list):
    #     #     return Response({"detail": "Expected a list of items."}, status=status.HTTP_400_BAD_REQUEST)
    #     serializer = self.get_serializer(data=request.data, many=True)  # Enable many=True for bulk
    #     serializer.is_valid(raise_exception=True)
    #     musics = serializer.save()
    #     return Response(MusicSerializer(musics, many=True).data, status=status.HTTP_201_CREATED)