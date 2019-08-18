from rest_framework.serializers import ModelSerializer
from .models import TouristSpot
from attractions.serializers import AttractionSerializer
from comments.serializers import CommentSerializer
from reviews.serializers import ReviewSerializer
from addresses.serializers import AddressSerializer
from rest_framework.fields import SerializerMethodField

class TouristSpotSerializer(ModelSerializer):

    attractions = AttractionSerializer(many=True)
    comments = CommentSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    address = AddressSerializer()
    test_description = SerializerMethodField()
    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'approved', 'image', 'attractions', 'comments', 'reviews', 'address', 'created_at', 'updated_at', 'test_description', 'test_description_two')

    def get_test_description(self, obj):
        return obj.name + ' - ' + obj.description