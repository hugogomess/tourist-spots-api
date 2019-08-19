from rest_framework.serializers import ModelSerializer
from .models import TouristSpot
from attractions.serializers import AttractionSerializer
from attractions.models import Attraction
from comments.serializers import CommentSerializer
from reviews.serializers import ReviewSerializer
from addresses.serializers import AddressSerializer
from addresses.models import Address
from rest_framework.fields import SerializerMethodField

class TouristSpotSerializer(ModelSerializer):

    attractions = AttractionSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    address = AddressSerializer()
    test_description = SerializerMethodField()
    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description', 'approved', 'image', 'attractions', 'comments', 'reviews', 'address', 'created_at', 'updated_at', 'test_description', 'test_description_two')

    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']

        address = validated_data['address']
        del validated_data['address']

        tourist_spot = TouristSpot.objects.create(**validated_data)
        self.create_attraction(attractions, tourist_spot)
        self.create_address(address, tourist_spot)

        tourist_spot.save()

        return tourist_spot

    def create_attraction(self, attractions, tourist_spot):
        for attraction in attractions:
            att = Attraction.objects.create(**attraction)
            tourist_spot.attractions.add(att)

    def create_address(self, address, tourist_spot):
        add = Address.objects.create(**address)
        tourist_spot.address = add
    
    def get_test_description(self, obj):
        return obj.name + ' - ' + obj.description