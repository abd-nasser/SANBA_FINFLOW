from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("auth_app.urls")),
    path("", include("directeur_app.urls")),
    path("", include("secretaire_app.urls")),
    path("", include("employee_app.urls")),
    path("", include("comptable_app.urls")),
    path("", include("client_app.urls")),
    path("", include("chantier_app.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)