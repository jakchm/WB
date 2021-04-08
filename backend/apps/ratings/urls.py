from django.urls import path
from .views import RatingsView, RatingsPerADVView, RatingsPerIDView

app_name = 'ratings'

urlpatterns = [
    path('', RatingsView.as_view(), name="ratings_view"),
    path('id/<int:pk>/', RatingsPerIDView.as_view(), name="ratings_per_id_view"),
    path('adv/<int:pk>/', RatingsPerADVView.as_view(), name="ratings_per_adv_view"),
]