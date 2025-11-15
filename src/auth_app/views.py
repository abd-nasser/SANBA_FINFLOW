from django.shortcuts import render, redirect
from .form import PersonnelRegisterForm
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def register_view(request):
    if request.method == "POST":
        try:
                form = PersonnelRegisterForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'inscription pour {form.cleaned_data.get("username")}, au post de {form.cleaned_data.get('post')}reussi ')
                    return redirect("interface/directeur.html")
                    
                
                else:
                    messages.error(request, "echec l'ors de l'inscription" )
                    return render(request, "auth_templates/register.html", {"form":form})
        except Exception as e:
            logger.error(f"erreur {e}")
             
    return render(request, "auth_templates/register.html", {"form":PersonnelRegisterForm()})


def login_view(request):
    pass