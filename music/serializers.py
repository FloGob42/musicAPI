from rest_framework import serializers
from .models import Music
from performer.models import Artist, Band, Performer
from django.contrib.contenttypes.models import ContentType



class MusicSerializer(serializers.ModelSerializer):
    performer = serializers.SerializerMethodField()
    
    class Meta:
        model = Music
        exclude= ['albums']

    def get_performer(self, obj):
        # Determine which model the interprete is (Artist or Band)
        if isinstance(obj.performer, Artist):
            return {'content_type': 'Artist', 'name': f"{obj.performer.first_name} {obj.performer.name}"}
        elif isinstance(obj.performer, Band):
            return {'content_type': 'Band', 'name': obj.performer.name}
        return None
    
    def create(self, validated_data):
        
        if isinstance(validated_data, list):
            musics = [Music(**item) for item in validated_data]
            return Music.objects.bulk_create(musics)
        else:
            # Fallback for single object creation
            return Music.objects.create(**validated_data)
        
    