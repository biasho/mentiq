# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('surveys/', include('surveys.urls')),
    path('api/v1/', include('surveys.api.urls')),
    # Định tuyến cho app Users
    path('users/', include('users.urls', namespace='users')),

   # Đổi 'oauth/' thành 'accounts/'
    path('accounts/', include('allauth.urls')),

    # Trang chủ & Trang tĩnh
    path('', include('pages.urls')),
]

# Phục vụ tệp media (avatar/files) trong môi trường phát triển (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)