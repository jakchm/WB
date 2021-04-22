from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField('get_author_name')
    class Meta:
        model = Comment
        fields = ('id','post','author_name','author','created_date','text')

    def get_author_name(self, post):
        if post.author == None:
            return "Anonymous"
        else:
            username = post.author.username
            return username


class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post','author','text')

    def validate(self, data):
        if len(data.get('text')) < 5:
            raise serializers.ValidationError("Comment should contain more than 5 characters")
        elif len(data.get('text')) >= 100:
            raise serializers.ValidationError("Comment should have less than 100 characters")
        else:
            return data
