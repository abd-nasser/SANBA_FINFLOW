from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #Sécurité
from django.views.generic import ListView, CreateView , DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib import messages


from .models import Chantier
from .models import Client  # Import the Client model
from .forms import ClientForm  # Import the ClientForm


class ClientListView(LoginRequiredMixin, ListView):
    """Récupère tous les liste de la base ,
        Les envoie au templates,
        Affiche le template
    
    """
    model = Client #le model utilsé
    template_name = "client_templates/client.html"
    context_object_name = "clients" #comment on l'appel dans le templates
    paginate_by = 20 # 20 clients par page 
    
    def get_queryset(self):
        """Personnalise quel client on souhaite afficher
           par defaut = Client.objects.all()
        """
        
        return Client.objects.all().order_by("nom")
    
    

class ClientCreateView(LoginRequiredMixin, CreateView):
    
    """Affichage automatique d'un formulaire vide
       valide les données qand on fait un submit
       crée le client en bd
       redirect vers list client 
    """
    
    model = Client
    form_class = ClientForm 
    template_name = "modal/ajouter_client.html"
    success_url = reverse_lazy("client_app:liste-client")
    
    def form_valid(self, form):
        """
        Méthode appelée quand le formulaire est valide
        On peut faire des actions supplémentaires ici
        """
        #Ajoute le commercial connecté automatiquement
        if hasattr(self.request.user, 'personnel'):
            form.instance.commercial_attache = self.request.user.personnel
        #Message de succès
        messages.success(self.request, f"Client {form.instance.nom} à été ajouté avec succès")
        
        #Sauvegarde le client et redirige
        return super().form_valid(form)
        
    

class ClientDetailView(LoginRequiredMixin, DetailView):
    """
    Cette vue  affiche les details d'un seul client
    elle recoit l'ID du client dans l'url
    """
    
    model = Client
    template_name = "client_templates/detail_client.html"
    context_object_name = 'client'
    
    def get_context_data(self, **kwargs):
        """On peut ajouter des données supplémentaires au template"""
        
        #Récupère le contexte de base (le client)
        context = super().get_context_data(**kwargs)
        
        #Ajoute les chantiers de ce client
        context["chantier"]=self.object.chantiers.all()
        return context
    
    
    
    
    
    
    
    
#FILTRER_CHANTIERS_HTMX-Filtre en temps réel avec htmx
def filter_chantiers_htmx(request):
    """Cette vue est appelée par HTMX quand on change un filtre
        Elle retourne Juste la liste des chantiers filtrés
    
    """
    
    # 1. Récupère tous les chantiers
    all_chantiers = Chantier.objects.all()
    
    # 2. on regarde les filter dans l'URL
    #EX: /?status=en_cours&client_id = 5
    
    #Filter par status
    status = request.GET.get('status_chantier') #récupère 'statut du chantier depuis l'URL
    if status:
        chantiers = all_chantiers.filter(status_chantier=status) #Filtre les chantiers par leur status
        
    #Filtre par client
    client_id = request.GET.get("client_id") #récupère 'client_id' depuis l'URL
    if client_id:
        chantiers = all_chantiers.filter(client_id=client_id) #Filtre les chantiers par leur clients
    
    # 3. on retourne JUSTE le html de la liste (pas toute la page)
    return render(request, 'partials/liste_chantier_partial.html',{
        "chantiers": chantiers
    })
    
