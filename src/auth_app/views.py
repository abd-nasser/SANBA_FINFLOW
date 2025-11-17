from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .form import PersonnelRegisterForm
from django.contrib import messages
from auth_app.models import Personnel, Post
from django.contrib.auth.forms import AuthenticationForm
import logging



logger = logging.getLogger(__name__)



def register_view(request):
    if request.method == "POST":
        try:
                form = PersonnelRegisterForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'inscription pour {form.cleaned_data.get("username")}, au post de {form.cleaned_data.get('post')}reussi ')
                    return redirect("directeur_app:directeur-view")
                    
                
                else:
                    messages.error(request, "echec l'ors de l'inscription" )
                    return render(request, "auth_templates/register.html", {"form":form})
        except Exception as e:
            logger.error(f"erreur {e}")
             
    return render(request, "auth_templates/register.html", {"form":PersonnelRegisterForm()})



def login_view(request):
    if request.method == "POST":
        try:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                personnel = get_object_or_404(Personnel, username=user.username, password=user.password)
                
                if user.is_superuser or personnel.post.nom == "Directeur" and  personnel.post.nom != "Secretaire" and  personnel.post.nom !="Employee":
                    login(request, user)
                    return redirect("directeur_app:directeur-view")
                
                elif personnel.post.nom =="Secretaire" and personnel.post.nom !="Directeur"and  personnel.post.nom !="Employee":
                    login(request, user)
                    return redirect("secretaire_app:secretaire-view")
                
                elif  personnel.post.nom =="Employee" and personnel.post.nom != "Directeur" and  personnel.post.nom !="Secretaire":
                    login(request, user)
                    return redirect("employee_app:employee-view")
            else:
                ctx ={"form": form}
                return render(request, "auth_templates/login.html", ctx)
        except Exception as e:
            logger.error(f"erreur{e}")
            
  
    return render(request,"auth_templates/login.html",{"form":AuthenticationForm()})
            
            
        
  