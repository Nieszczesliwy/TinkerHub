from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api-auth/", include('rest_framework.urls')),
    path("admin/", admin.site.urls),
    path("auth/", include('authentication.urls')),
    path("", include('articles.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)