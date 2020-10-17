from rest_framework import serializers
from .models import Board, Comment


class BoardSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source='user.username', read_only=True)

    comments = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = [
            'id',
            'username',
            'category',
            'title',
            'content',
            'img_path',
            'created',
            'views',
            'comments',
        ]
    
    def get_comments(self, board):
        return Comment.objects.filter(board=board).count()

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['board', 'username', 'content', 'created']
