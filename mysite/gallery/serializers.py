from rest_framework import serializers
from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source='user.username', read_only=True)

    class Meta:
        model = Gallery
        fields = [
            'id',
            'username',
            'title',
            'content',
            'img_path',
            'created',
            'views',
        ]
