from django.urls import path
from .views import CommentView, CommentPerADVView, CommentPerIDView

app_name = 'comment'

urlpatterns = [
    path('', CommentView.as_view(), name="comment_view"),
    path('id/<int:pk>/', CommentPerIDView.as_view(), name="comment_per_id_view"),
    path('adv/<int:pk>/', CommentPerADVView.as_view(), name="comment_per_adv_view"),
]