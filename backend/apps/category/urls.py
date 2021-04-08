from django.urls import path
from .views import CategoryView, SubCategoryPerCategoryView

app_name = 'category'

urlpatterns = [
    path('', CategoryView.as_view(), name="category_view"),
    path('cat/<int:pk>/', SubCategoryPerCategoryView.as_view(), name="subcategory_per_category_view"),
]