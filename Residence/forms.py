from django import forms
from django.forms import ModelForm, TextInput,PasswordInput,EmailInput,IntegerField,DateInput
from Residence.models import sondage,alerte

class SondageForm(forms.ModelForm):
    
    class Meta:
        model = sondage
        exclude=('create_at','batiment')
        widgets = {
            'question': TextInput(attrs={'class':'form-control','id':'inputName','placeholder':'Nom Batiment'}),
            'content': TextInput(attrs={'class':'form-control','id':'inputNbrApp','placeholder':'Nombre Appartement'}),
            'finSondage': DateInput(attrs={'class':'form-control pickadate-translations'}),
        }
class AlerteForm(forms.ModelForm):
    
    class Meta:
        model = alerte
        exclude=('create_at','vue','etat','batiment','habitant')
        widgets = {
            'cause': forms.Textarea(attrs={'class':'form-control','id':'inputName','placeholder':'Nom Batiment'}),
        }