from django import forms
from .models import RapportDepense

class RapportDepenseForm(forms.ModelForm):
    class Meta:
        model = RapportDepense
        fields = ["type_depense"]
        
    