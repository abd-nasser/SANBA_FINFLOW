from django.shortcuts import render
from .form import RapportDepenseForm
from .models import RapportDepense


def rapport_depense_view(request):
    
    if request.method == "POST":
        form = RapportDepenseForm(request.POST)
        
            
        materiau_article = request.POST.get("materiau_article")
        prix_unitaire = request.POST.get("prix_unitaire")
        chantier = request.POST.get("chantier")
        quantite = request.POST.get("quantité")
        fournisseur = request.POST.get("fournisseur")
        photo_facture = request.POST.get("photo_facture")
        
        print("requet recu")
        if form.is_valid():
             
            rapport = RapportDepense.objects.create(
                
                    employee=request.user,
                    type_depense=form.cleaned_data.get("type_depense"),
                    materiau_article=materiau_article,
                    prix_unitaire=prix_unitaire,
                    chantier=chantier,
                    quantité=quantite,
                    fournisseur=fournisseur,
                    facture=photo_facture      
            
        )
        rapport.save()
        print("rapport save")
    ctx = {"form":RapportDepenseForm()}
    return render(request, "employee_templates/employee.html", ctx)
    
        
        
        
        
        
        
        
