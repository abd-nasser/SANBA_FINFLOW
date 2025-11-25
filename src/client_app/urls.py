from django.urls import path
from . import views

app_name = 'client_app'

urlpatterns = [
    path("client/", views.ClientListView.as_view(), name="liste-client"),
    path("ajouter-client/", views.ClientCreateView.as_view(), name="ajouter-client"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail-client"),
    path('filter-chantiers', views.filter_chantiers_htmx, name="filter-chantiers")
        
         ]

