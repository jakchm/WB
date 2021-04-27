from django.shortcuts import render
from django.contrib.auth import login
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, UserInfoSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from apps.core.models import Post

# Create your views here.
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializers = AuthTokenSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class UserInfoAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (IsAuthenticated,)  

    def perform_create(self, serializer):
        serializer.save(total_posts=len(Post.objects.filter(author=AuthToken.objects.get(token_key=request.META.get('HTTP_AUTHORIZATION')[6:14]).user.id)))

    def get_queryset(self ,*args, **kwargs):
        return User.objects.filter(id=AuthToken.objects.get(token_key=self.request.META.get('HTTP_AUTHORIZATION')[6:14]).user.id)


