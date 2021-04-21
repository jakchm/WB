from django.urls import path
from .views import CommentPerPostView, CommentPerIDView, AddCommentView

app_name = 'comment'

urlpatterns = [
    path('id/<int:pk>/', CommentPerIDView.as_view(), name="comment_per_id_view"),
    path('post/<int:pk>/', CommentPerPostView.as_view(), name="comment_per_post_view"),
    path('add/', AddCommentView.as_view(), name="add_comment_view"),
]