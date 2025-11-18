from django.urls import path
from . import views

app_name ="directeur_app"

urlpatterns = [
    path("interface-directeur",views.directeur_view, name='directeur-view'),
    path("approuver/<int:demande_id>/demande", views.approuve_demande_view, name="approuver-demande"),
    path("refuser/<int:demande_id>/demande", views.refuse_demande_view, name="refuser-demande"),
    path("ajouter-fond", views.ajouter_fond, name="ajouter-fond")
]

