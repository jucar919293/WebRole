"""RoleBoardGames URL Configuration """

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls','users'), namespace='users')),
    path('', include(('home.urls', 'home'), namespace='home'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
