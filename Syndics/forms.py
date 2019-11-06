from django import forms
from django.forms import ModelForm, TextInput,PasswordInput,EmailInput,IntegerField
from Accounts.models import Batiment
from Syndics.models import documentBatiment

class BatimentForm(forms.ModelForm):
    
    class Meta:
        model = Batiment
        exclude=('user',)
        widgets = {
            'nom': TextInput(attrs={'class':'form-control','id':'inputName','placeholder':'Nom Batiment'}),
            'nbrApp': TextInput(attrs={'class':'form-control','id':'inputNbrApp','placeholder':'Nombre Appartement','type':'number'}),
            'nbrResidant': TextInput(attrs={'class':'form-control','id':'inputNbrResidant','placeholder':'Nombre de Residant','type':'number'}),
            'ville': TextInput(attrs={'class':'form-control','id':'inputVille','placeholder':'Ville'}),
            'quartier': TextInput(attrs={'class':'form-control','id':'inputquartier','placeholder':'Quartier'}),
        }

class DocForm(forms.ModelForm):

    class Meta:
        model = documentBatiment
        fields = ['title', 'cover']