from django.db import models

class FondDisponibe(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_ajout = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.montant}--{self.date_ajout}'
