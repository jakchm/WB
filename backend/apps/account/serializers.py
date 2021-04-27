from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ForbiddenUserNames
from apps.core.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    def validate(self, data):
        username = data.get('username')
        if len(username) > 36 or len(username) < 3:
            raise serializers.ValidationError("Username should contain between 3 to 36 characters")

        if ForbiddenUserNames.objects.filter(name=username):
            raise serializers.ValidationError("This name is forbidden!")

        if User.objects.filter(username=username):
            raise serializers.ValidationError("Somebody use this name")   
        
        email = data.get('email')
        if "@" not in email or "." not in email or len(email) < 6:
            raise serializers.ValidationError("This is not an email address")

        if User.objects.filter(email=email):
            raise serializers.ValidationError("Somebody use this email") 


        return data

class UserInfoSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_email')
    username = serializers.SerializerMethodField('get_username')
    posts = serializers.SerializerMethodField('get_total_post')
    class Meta:
        model = User
        fields = ('id','username', 'email','posts')
        extra_kwargs = {'total_posts': {'read_only':True}}

    def get_email(self, user):
        if user.email == None:
            return None
        else:
            email = user.email
            return email

    def get_username(self, user):
        if user.username == None:
            return None
        else:
            username = user.username
            return username

    def get_total_post(self, user):
        if Post.count_posts_of(user) == None:
            return None
        else:
            return Post.count_posts_of(user)


    




    