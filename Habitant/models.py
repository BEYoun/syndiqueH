from django.db import models
from django.contrib.auth.models import User
from Residence.models import sondage
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime 
from Accounts.models import Profil,Batiment
# Create your models here.
class vote(models.Model):
    sondage = models.ForeignKey(sondage , on_delete=models.CASCADE)
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

class cotisationValidation(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date = models.DateField(blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    etat = models.BooleanField(default=False)
    reponse = models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)
