from django.shortcuts import render
from .models import Ratings
from .serializers import RatingsSerializer
from rest_framework import generics

# Create your views here.

class RatingsView(generics.ListAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

class RatingsPerIDView(generics.ListAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

    def get_queryset(self, *args, **kwargs):
        return Ratings.objects.filter(id=self.kwargs['pk'])

class RatingsPerADVView(generics.ListAPIView):
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer

    def get_queryset(self, *args, **kwargs):
        return Ratings.objects.filter(advert=self.kwargs['pk'])