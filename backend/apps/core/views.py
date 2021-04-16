from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from knox.models import AuthToken

# Create your views here.

class PostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostIDView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(id=self.kwargs['pk'])

class PostCategoryView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category=self.kwargs['pk'])

class PostSubCategoryView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(subcategory=self.kwargs['pk'])

class AddPostView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)   

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        request.data["author"] = AuthToken.objects.get(token_key=request.META.get('HTTP_AUTHORIZATION')[6:14]).user.id
        return self.create(request, *args, **kwargs)



