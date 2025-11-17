from django.urls import path
from . import views

app_name = "secretaire_app"

urlpatterns = [
    path("interface-secretaire", views.demande_decaissement_view, name="secretaire-view"),
    #path("list-demande", views.list_demande_view, name="list-demande")
]
