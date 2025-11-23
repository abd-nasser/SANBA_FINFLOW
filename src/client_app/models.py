from django.db import models

from auth_app.models import Personnel
from django.utils import timezone


class Client(models.Model):
    """
    toutes les informations relatives aux clients
    """
    #choix possible pour le type de client
    TYPE_CLIENT_CHOICES = [
        ('particulier', 'Particulier'),
        ('entreprise', 'Entreprise'),
        ('institution', 'Institution publique'),
        ("promoteur", "Promoteur immobilier"), #ceux qui font dans le batiment
        ('autre', 'Autre')
    ]
    
    #type de batiment à travailler
    SECTEUR_ACTIVITE_CHOICES = [
        ('residential', 'Résidentiel'), #Maisons, appartements
        ('commercial', 'Commercial'), #Bureaux, magasins
        ('industriel', 'Industriel'), #Usines, entrepôts
        ('agricole', 'Agricole'), #Ferme, installations agricoles
        ('public', 'Public'),   #Écoles, hôpitaux, bâtiments gouvernementaux 
    ]
    
    #comment le client a connu l'entreprise
    SOURCE_CLIENT_CHOICES = [
        ('recommendation', 'Recommandation'),
        ('site_web', 'Site Web'),
        ('reseaux_sociaux', 'Réseaux Sociaux'),
        ('publicite', 'Publicité'),
        ('ancien_client', 'Ancien Client'),
        ('autre', 'Autre'),
        ('salon', 'Salon Professionnel'),
        ("autre", "Autre")
    ]
    
    #info principales du client
    type_client = models.CharField(max_length=50, choices=TYPE_CLIENT_CHOICES)
    
    #raison sociale = nom de l'entreprise
    raison_sociale = models.CharField(max_length=200, null=True, blank=True)
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=20)
    telephone_secondaire = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    adresse = models.TextField()
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100, null=True, blank=True)
    pays = models.CharField(max_length=100)
    
    #INFOS BUSINESS 
    #sectreur d'activité du client
    secteur_activite = models.CharField(max_length=50, choices=SECTEUR_ACTIVITE_CHOICES, null=True, blank=True)
    source_client = models.CharField(max_length=50, choices=SOURCE_CLIENT_CHOICES, null=True, blank=True)
    
    #note_internes remarque sur le client
    notes_internes = models.TextField(null=True, blank=True)
    potentiel_client = models.CharField(max_length=20, 
                                        choices=[
                                                    ('faible', 'Faible'), #petit budget
                                                    ('moyen', 'Moyen'), #budget moyen
                                                    ('élevé', 'Élevé') #gros budget
                                                ], 
                                        null=True, blank=True, 
                                        default='moyen')
    
    #Suivi de la RElation 
    #date_premier_contact
    date_premier_contact = models.DateField(null=True, blank=True)
    
    #commercial_attache = le commercial qui suit le client
    commercial_attache = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True)
    
    #est fidel = un client qui revient souvent
    est_fidel = models.BooleanField(default=False)
    
    #STATS AUTOMATIQUES
    #total_contrats = nombre total de contrats signés avec ce client
    total_contrats = models.IntegerField(default=0)
    
    #chiffre_affaires = montant total facturé à ce client
    chiffre_affaires_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    class Meta:
        """configuration spécial pour django"""
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    def __str__(self):
        """affichage dans l'admin"""
        if self.type_client == 'Entreprise':
            return f"{self.raison_sociale} - {self.telephone} -{self.ville} "
        else:
            return f"{self.nom} -{self.prenom} - {self.telephone} -{self.ville} "


class Chantier(models.Model):
    
    """
    toutes les informations relatives aux chantiers
    """
    TYPE_TRAVAUX_CHOICES = [
        ("charpente_metallique", "Charpente Métallique"),
        ("toiture_tole", "Toiture en Tôle"),
        ("couverture", "Couverture"),
        ("isolation", "Isolation"),
        ("ventilation", "Ventilation"),
        ("etancheite", "Étanchéité"),
        ("garde_corps", "Garde-Corps"),
        ("escalier_metal", "Escalier en Métal"),
        ("porte_grillee", "Porte/Grille Métallique"),
        ("mixte", "Travaux Mixtes"),
        ("autre", "Autre")
    ]


    TYPE_BATIMENT_CHOICES = [
        ("maison_individuelle", "Maison Individuelle"),
        ("appartement", "Appartement"),
        ('entrepot', 'Entrepôt'),
        ('usine', 'Usine'),
        ('bureau', 'Bureau'),
        ('commerce', 'Commerce'),
        ('ferme', 'Batiment Agricole'),
        ('batiment_public', 'Batiment Public'),
        ('autre', 'Autre')
    
    ]

    STATUS_CHANTIER_CHOICES = [
        ("devis","Devis en Cours"),
        ('planification', 'Planification'),
        ('en_cours', 'En Cours'),
        ('suspendu', 'Suspendu'),
        ('termine', 'Terminé'),
        ('facturee', 'Facturée'),
        ('paye', 'Payée'),
        ('annule', 'Annulé')
    ]

    client = models.ForeignKey(Client, related_name="chantiers", on_delete=models.CASCADE)
    
    #reférence unique du chantier
    reference = models.CharField(max_length=100, unique=True)
    
    #nom_chantier = un nom facile à retenir pour le chantier
    nom_chantier = models.CharField(max_length=200)
    
    #LOCALISATION PRÉCISE
    adresse_chantier = models.TextField()
    ville_chantier = models.CharField(max_length=100)
    quartier_chantier = models.CharField(max_length=100, null=True, blank=True)
    pays_chantier = models.CharField(max_length=100)
    
    #gps_latitude et longitude = position gps du chantier
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    #caractéristiques du chantier
    type_travaux = models.CharField(max_length=50, choices=TYPE_TRAVAUX_CHOICES)
    type_batiment = models.CharField(max_length=50, choices=TYPE_BATIMENT_CHOICES)
    surface_totale = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) #en m2
    
    #hauteur_batiment = hauteur totale du batiment en metres
    hauteur_batiment = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    
    #desceription = description détaillée du chantier
    description_detaille = models.TextField(null=True, blank=True)
    
    #planning 
    #date_debut_prevue et date_fin_prevue = dates prévues pour le chantier
    date_debut_prevue = models.DateField(null=True, blank=True)
    date_fin_prevue = models.DateField(null=True, blank=True)   
    
    #date_debut_reelle et date_fin_reelle = dates réelles du chantier
    date_debut_reelle = models.DateField(null=True, blank=True)
    date_fin_reelle = models.DateField(null=True, blank=True)
    
    #duree_estimee = durée estimée du chantier en jours
    duree_estimee = models.IntegerField(null=True, blank=True)  
    
    #EQUIPE 
    chef_de_chantier = models.ForeignKey(Personnel, related_name="chantiers_chef", on_delete=models.SET_NULL, null=True, blank=True)
    
    #equipe_affectee = une liste des employés affectés au chantier
    equipe_affectee = models.ManyToManyField(Personnel, related_name="chantiers_participants", blank=True)
    
    #STATUT ET SUIVI FINANCIER
    #budget_total = budget total alloué au chantier
    budget_total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    #cout_materiaux_estime = coût estimé des matériaux
    cout_materiaux_estime = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    #cout_main_oeuvre_estime = coût estimé de la main d'oeuvre
    cout_main_oeuvre_estime = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    #marge_beneficiaire_estimee = marge bénéficiaire estimée
    marge_beneficiaire_estimee = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    #STATUS ET  SUIVI
    status_chantier = models.CharField(max_length=50, choices=STATUS_CHANTIER_CHOICES, default='devis')
    
    #priorité = priorité du chantier
    priorite = models.CharField(max_length=20, 
                               choices=[
                                           ('basse', 'Basse'),
                                           ('normale', 'Normale'),
                                           ('haute', 'Haute'),
                                           ('urgente', 'Urgente')
                                       ], 
                               default='normale')
    
    #DOCUMENTS
    # plans_et_specifications = fichiers liés aux plans du chantier
    plans_joins = models.BooleanField(default=False)
    photos_avant = models.BooleanField(default=False)
    photos_apres = models.BooleanField(default=False)
    
    #METADATA AUTOMATIQUE
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        """configuration spécial pour django"""
        verbose_name = "Chantier"
        verbose_name_plural = "Chantiers"
    
    def __str__(self):
        """affichage dans l'admin"""
        return f"{self.reference} - {self.nom_chantier} - {self.client}"
    
    
    def calculer_progression(self):
        """Calcule combien de pourcentage du chantier est terminé
        """
        return 0 # a ameliorer plus tard
    
    @property
    def est_en_retard(self):
        """Vérifie si le chantier est en retard par rapport à la date de fin prévue
        """
        if self.date_fin_prevue and self.date_fin_reelle:
            return self.date_fin_reelle > self.date_fin_prevue
        return False
    


class Contrat(models.Model):
    """tout les regle du jeu"""
    MODE_PAIEMENT_CHOICES = [
        ("comptant", "Comptant"),
        ('tranche', "Tranche"),
        ("credit", "Crédit"),
        ("autre", "Autre")
    ]
    
    #LIEN AVEC LE CHANTIER
    #chantier= à quel chantier ce contrat est lié
    chantier = models.OneToOneField(Chantier,related_name="chantiers", on_delete=models.CASCADE)
    
    #numéro unique pour contrat 
    referenre_contrat = models.CharField(max_length=50, unique=True)
    
    #quand le contrat été signé
    date_signature = models.DateField(null=True, blank=True)
    
    #comment le client souhaite payer
    mode_paiement = models.CharField(max_length=20, choices=MODE_PAIEMENT_CHOICES, default="comptant")
    
    #montant total du contrat
    montant_total = models.DecimalField(max_digits=12, decimal_places=2)
    
    #combien de % le client paye au debut
    acompte_pourcentage = models.DecimalField(max_digits=5, decimal_places=2, default=30)
    
    #en combien de fois il paye le reste 
    nombre_tranches = models.IntegerField(default=1)
    
    #SUIVIS DES PAIEMENTS
    #montant_encaisse = combien a été payé jusqu'à présent
    montant_encaisse = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    #datze_du_dernier_paiement = date du dernier paiement reçu
    date_du_dernier_paiement = models.DateField(null=True, blank=True)
    
    #DOCUMENTS IMPOERTANTS
    contrat_pdf = models.FileField(upload_to="contrats/", null=True, blank=True)
    
    #devis_initial = le premier qu'on a fait
    devis_initial = models.FileField(upload_to="devis/", null=True, blank=True)
    
    #CLAUSES SPECIALES
    # garanttie_mois = combien de mois on garantis notre travail
    garantie_mois = models.IntegerField(default=12)
    
    #notes_contractuelles = détails importants du contract
    notes_contractuelles = models.TextField(null=True, blank=True)
    
    class Meta:
        """configuration spécial pour django"""
        verbose_name = "Contrat"
        verbose_name_plural = "Contrats"
        
    def __str__(self):
        """affichage dans l'admin"""
        return f"Contrat {self.referenre_contrat} pour Chantier {self.chantier.nom_chantier}"
    
    @property
    def solde_restant(self):
        """Calcule combien il reste  à payer sur le contrat
        """
        return self.montant_total - self.montant_encaisse
    
    @property
    def pourcentage_encaisse(self):
        """Calcule le pourcentage du contrat qui a été payé
        """
        if self.montant_total > 0:
            return (self.montant_encaisse / self.montant_total) * 100
        return 0
    
    
    @property
    def montant_acompte(self):
        """Calcule le montant de l'acompte à payer
        """
        return (self.acompte_pourcentage / 100) * self.montant_total
    
    @property
    def est_signed(self):
        """Vérifie si le contrat a été signé
        """
        return self.date_signature is not None
    
    def enregistrer_paiement(self, montant_paye):
        """Enregistre un paiement fait par le client
        """
        self.montant_encaisse += montant_paye
        self.date_du_dernier_paiement = timezone.now().date()
        self.save()
        
        if self.montant_encaisse >= self.montant_total:
            # Contrat entièrement payé
            self.chantier.status_chantier = 'paye'
            self.chantier.save()
            
class TranchePaiement(models.Model):
    """pour les paiements en plusieurs tranches
    chaque tranche = une date ou le client doit payer
    
    """
    # contrat = à quel contrat cette tranche est liée
    contrat = models.ForeignKey(Contrat, related_name="tranches", on_delete=models.CASCADE)
    
    #numéro de la tranche
    numero_tranche = models.IntegerField()
    
    #montant = combien d'argent pour cette tranche
    montant = models.DecimalField(max_digits=12, decimal_places=2)
    
    #date_prevue = quand le client doit payer cette tranche
    date_prevue = models.DateField()
    
    #date_reelle = quand le client a réellement payé cette tranche
    date_reelle = models.DateField(null=True, blank=True)
    
    #est_payee = si cette tranche a été payée
    est_payee = models.BooleanField(default=False)
    
    #motif = pourquoi cette tranche ...(ex: retard, problème technique, etc.)
    motif = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name = "Tranche de Paiement"
        verbose_name_plural = "Tranches de Paiement"
        ordering = ['numero_tranche']
        
    def __str__(self):
        return f"Tranche {self.numero_tranche} du Contrat {self.contrat.referenre_contrat}"
    
    def marquer_comme_payee(self):
        """Marque cette tranche comme payée et enregistre la date réelle de paiement"""
        self.est_payee = True
        self.date_reelle = timezone.now().date()
        self.save()
        
        # met à jour le contrat parent 
        self.contrat.montant_encaisse += self.montant
        self.contrat.date_du_dernier_paiement = self.date_reelle
        self.contrat.save()
          