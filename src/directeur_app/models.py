from django.db import models

class FondDisponibe(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
