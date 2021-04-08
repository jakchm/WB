from rest_framework import serializers
from apps.core.models import Post
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField('get_author_name')

    class Meta:
        model = Post
        fields = ('id','author','author_name','title','text','category','subcategory','created_date','image')

    def get_author_name(self, advert):
        if advert.author == None:
            return None
        else:
            username = advert.author.username
            return username
    



