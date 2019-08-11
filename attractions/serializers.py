from rest_framework.serializers import ModelSerializer
from .models import Attraction

class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'opening_time', 'close_time', 'minimum_age', 'created_at', 'updated_at')