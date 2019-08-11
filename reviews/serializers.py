from rest_framework.serializers import ModelSerializer
from .models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'review', 'review_points', 'created_at', 'updated_at')