from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/", include("user.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), for debug toolbar
        path(
            settings.DOCS_URL,
            include_docs_urls(
                title="TBM MUSIC API Docs",
                description="API documentation for TBM",
            ),
        ),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
