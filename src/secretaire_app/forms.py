from django import forms
from .models import DemandeDecaissement


class DemandeDecaissementForm(forms.ModelForm):
    class Meta:
        model = DemandeDecaissement
        fields = "__all__"
        exclude = ["status"]