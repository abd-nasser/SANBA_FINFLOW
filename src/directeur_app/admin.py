from django.contrib import admin
from .models import FondDisponibe

@admin.register(FondDisponibe)
class AdminFondDisponible(admin.ModelAdmin):
    list_display = ["montant", "date_ajout"]
    
