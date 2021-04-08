from django.shortcuts import render
from .serializers import CategorySerializer, SubCategorySerializer
from .models import Category, SubCategory
from rest_framework import generics

# Create your views here.

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryPerCategoryView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self, *args, **kwargs):
        return SubCategory.objects.filter(category=self.kwargs['pk'])
