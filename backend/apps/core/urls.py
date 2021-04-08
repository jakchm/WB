from django.urls import path
from .views import PostsView, PostIDView, PostCategoryView, AddPostView

app_name = 'core'

urlpatterns = [
    path('', PostsView.as_view(), name="posts_view"),
    path('id/<int:pk>/', PostIDView.as_view(), name="post_per_id_view"),
    path('category/<int:pk>/', PostCategoryView.as_view(), name="post_per_category_view"),
    path('add/', AddPostView.as_view(), name="add_post_view")
]