from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer, AddCommentSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken

# Create your views here.

class CommentPerPostView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(post=self.kwargs['pk'])

class CommentPerIDView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(id=self.kwargs['pk'])


class AddCommentView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)   

    queryset = Comment.objects.all()
    serializer_class = AddCommentSerializer

    def post(self, request, *args, **kwargs):
        request.data["author"] = AuthToken.objects.get(token_key=request.META.get('HTTP_AUTHORIZATION')[6:14]).user.id
        return self.create(request, *args, **kwargs)
