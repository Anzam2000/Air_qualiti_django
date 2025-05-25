
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from air_4_you.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('air/', include('air_4_you.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)