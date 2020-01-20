from django.conf import settings

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name="core"),
    path('eventos/', include('event.urls', namespace="events")),
    path('usuarios/', include('account.urls', namespace="users")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    from django.urls import include
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns