
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("auth_app.urls")),
    path("", include("directeur_app.urls")),
    path("", include("secretaire_app.urls"))
]
