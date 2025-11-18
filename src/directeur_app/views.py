from django.shortcuts import render, get_object_or_404, redirect
from .models import FondDisponibe, Historique_dajout_fond
from secretaire_app.models import DemandeDecaissement
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


def directeur_view(request):
    fond = get_object_or_404(FondDisponibe, id=1)
    list_demande = DemandeDecaissement.objects.all().order_by("-date")
    
    ctx = {
            "list_demande": list_demande,
            "fond":fond.montant
           }
    return render(request, "directeur_templates/directeur.html", ctx)




def ajouter_fond(request):
    fond = get_object_or_404(FondDisponibe, id=1)
    
    if request.method == 'POST':
        try:
            fond_aj = request.POST.get("montant")
            fond.montant +=int(fond_aj)
            fond.save()
            historique_de_fond = Historique_dajout_fond.objects.create(nom=request.user, montant=fond_aj)
            historique_de_fond.save()
            messages.success(request, f"vous venez d'ajouter la somme de {fond_aj} au fond disponible ! Nouveau Capitale est de : {fond.montant}")
            return redirect("directeur_app:directeur-view")
            
        except Exception as e:
            logger.error(f"error{e}")
            
    return render(request, "partials/ajouter_fond.html")
            
        
            
            

def approuve_demande_view(request, demande_id):
    demande = get_object_or_404(DemandeDecaissement, id=demande_id)
    demande.status="Approuvée"
    demande.save()
    return redirect("directeur_app:directeur-view")
    

def refuse_demande_view(request, demande_id):
    demande = get_object_or_404(DemandeDecaissement, id=demande_id)
    demande.status="Refusée"
    demande.save()
    return redirect("directeur_app:directeur-view")