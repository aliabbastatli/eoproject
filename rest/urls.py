from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('api/esp/', include('esp.api.urls', namespace = 'esp')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)