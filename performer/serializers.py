from rest_framework import serializers
from .models import Artist, Band, Performer
from music.models import Music

class ArtistSerializer(serializers.ModelSerializer):
    # performer_type = serializers.CharField(default='Artist')

    class Meta:
        model = Artist
        fields = [ 'first_name', 'name', 'genres', 'origin', 'birth_date']

    def create(self, validated_data):
        
        if isinstance(validated_data, list):
            artists = [Artist(**item) for item in validated_data]
            return Artist.objects.bulk_create(artists)
        else:
            # Fallback for single object creation
            return Artist.objects.create(**validated_data)

class BandSerializer(serializers.ModelSerializer):
    # performer_type = serializers.CharField(default='Band', read_only = True)
    

    class Meta:
        model = Band
        fields = ['name', 'genres', 'origin', 'formation_year']

    def create(self, validated_data):
        
        if isinstance(validated_data, list):
            bands = [Band(**item) for item in validated_data]
            return Band.objects.bulk_create(bands)
        else:
            # Fallback for single object creation
            return Band.objects.create(**validated_data)

class PerformerSerializer(serializers.ModelSerializer):
    performer_type = serializers.SerializerMethodField()

    musics = serializers.HyperlinkedRelatedField(read_only=True, view_name='music-detail')

    class Meta:
        model = Performer
        fields = ['id', 'name', 'genres', 'origin', 'performer_type', 'musics']

    def get_performer_type(self, obj):
        if isinstance(obj, Artist):
            return "Artist"
        elif isinstance(obj, Band):
            return "Band"
        
    def get_music_links(self, obj):
        musics = Music.objects.filter(performer=obj, read_only= True) 
        return [{'title': music.title, 'url': f'/musics/{music.id}/'} for music in musics]