from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ForbiddenUserNames


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
