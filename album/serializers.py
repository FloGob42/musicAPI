from rest_framework import serializers
from .models import Album
from performer.models import Artist, Band

class AlbumSerializer(serializers.ModelSerializer):
    interprete = serializers.SerializerMethodField()
    
    class Meta:
        model = Album
        fields = '__all__'

    def get_interprete(self, obj):
        # Determine which model the interprete is (Artist or Band)
        if isinstance(obj.interprete, Artist):
            return {'type': 'Artist', 'name': f"{obj.interprete.first_name} {obj.interprete.name}"}
        elif isinstance(obj.interprete, Band):
            return {'type': 'Band', 'name': obj.interprete.name}
        return None