from django.db import models
from auth_app.models import Personnel



class DemandeDecaissement(models.Model):
    STATUS = [
        ("Approuvée"," approuvée"),
         ("En attente", "en attente"),
         ("Refusée", "refusée"),
         ("Decaissé", "Decaissé")
    ]
    
    nom = models.ForeignKey(Personnel, on_delete=models.PROTECT)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    chantier = models.CharField(max_length=200, null=True, blank=True)
    motif = models.TextField()
    status = models.CharField(max_length=100,choices=STATUS, default="En attente")
    date = models.DateTimeField(auto_now=True)
    
    
