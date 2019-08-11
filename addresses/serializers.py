from rest_framework.serializers import ModelSerializer
from .models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'line_one', 'line_two', 'city', 'state', 'country', 'created_at', 'updated_at')