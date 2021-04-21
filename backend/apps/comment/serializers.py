from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField('get_author_name')
    class Meta:
        model = Comment
        fields = ('id','post','author_name','author','created_date','text')

    def get_author_name(self, advert):
        if advert.author == None:
            return None
        else:
            username = advert.author.username
            return username


class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post','author','text')