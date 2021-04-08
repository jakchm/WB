
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('apps.core.urls')),
    path('category/', include('apps.category.urls')),
    path('ratings/', include('apps.ratings.urls')),
    path('comment/', include('apps.comment.urls')),
    path('account/', include('apps.account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
