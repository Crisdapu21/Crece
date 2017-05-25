from django.conf import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^', include('usuarios.urls', namespace='usuarios')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
