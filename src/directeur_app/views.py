from django.shortcuts import render, get_object_or_404, redirect
from secretaire_app.models import DemandeDecaissement

def directeur_view(request):
    ctx = {"list_demande": DemandeDecaissement.objects.all()
           }
    
    return render(request, "directeur_templates/directeur.html", ctx)


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