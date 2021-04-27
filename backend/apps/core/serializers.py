from rest_framework import serializers
from apps.core.models import Post
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField('get_author_name')
    category_name = serializers.SerializerMethodField('get_category_name')
    subcategory_name = serializers.SerializerMethodField('get_subcategory_name')

    class Meta:
        model = Post
        fields = ('id','author','author_name','title','text','category','category_name','subcategory','subcategory_name','created_date','image')

    def get_author_name(self, post):
        if post.author == None:
            return None
        else:
            username = post.author.username
            return username

    def get_category_name(self, post):
        if post.category == None:
            return "Anonymous"
        else:
            category = post.category.name
            return category

    def get_subcategory_name(self, post):
        if post.subcategory == None:
            return "Not-specifed"
        else:
            subcategory = post.subcategory.name
            return subcategory

    def validate(self, data):
        if len(data.get('text')) < 500:
            raise serializers.ValidationError("Text should contain more than 500 characters")
        elif len(data.get('text')) >= 5000:
            raise serializers.ValidationError("Text should have less than 5000 characters")
        elif len(data.get('title')) < 10:
            raise serializers.ValidationError("Title should contain more than 10 characters")
        elif len(data.get('title')) > 60:
            raise serializers.ValidationError("Title should have less than 60 characters")
        elif not data.get('image'):
            raise serializers.ValidationError("Image is required")            
        elif data.get('image').size > 10485760:
            raise serializers.ValidationError("Image should have maximum 10 MB")
        else:
            w, h = get_image_dimensions(data.get('image'))
            if h < 300:
                raise serializers.ValidationError("Wrong image size. Should be minimum 300 pixels!")
            return data
    



