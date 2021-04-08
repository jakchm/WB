from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import generics

# Create your views here.

class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentPerADVView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(advert=self.kwargs['pk'])

class CommentPerIDView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(id=self.kwargs['pk'])