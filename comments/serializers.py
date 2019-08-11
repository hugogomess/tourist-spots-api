from rest_framework.serializers import ModelSerializer
from .models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment', 'approved', 'created_at', 'updated_at')