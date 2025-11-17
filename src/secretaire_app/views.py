from django.shortcuts import render, redirect
from .forms import DemandeDecaissementForm
from .models import DemandeDecaissement
import logging

logger = logging.getLogger(__name__)




def demande_decaissement_view(request):
    if request.method == 'POST':
        try:
            form = DemandeDecaissementForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("secretaire_app:secretaire-view")
            else:
                ctx = {"form":form}
                return render(request, "secretaire_templates/secretaire.html",ctx)
        except Exception as e:
            logger.error(f'erreur {e}')
    list_demande = DemandeDecaissement.objects.all()
    ctx =  {"form":DemandeDecaissementForm(),
            "list_demande":list_demande} 
    return render(request, "secretaire_templates/secretaire.html",ctx)
            
            
       

