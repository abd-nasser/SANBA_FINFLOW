from django.urls import path
from . import views

app_name ="directeur_app"

urlpatterns = [
    path("",views.directeur_view,name='directeur-view'  )
]

