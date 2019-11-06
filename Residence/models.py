from django.db import models
from Accounts.models import Batiment,Profil
# Create your models here.
class sondage(models.Model):
    question = models.CharField(max_length=100)
    content = models.TextField()
    finSondage = models.DateTimeField()
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class reponseSondage(models.Model):
    rep = models.CharField(max_length=30)
    sondage = models.ForeignKey(sondage , on_delete=models.CASCADE)
    nombreVote = models.IntegerField(default=0)
class cotisation(models.Model):
    habitant = models.ForeignKey(Profil , on_delete=models.CASCADE)
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    prix = models.IntegerField()
class assemblee(models.Model):
    titre = models.CharField(max_length=20)
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    description = models.TextField()
    type_ass = models.CharField(max_length=10)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
class ordreAssemblee(models.Model):
    question = models.CharField(max_length=100)
    ass = models.ForeignKey(assemblee , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class alerte(models.Model):
    cause = models.CharField(max_length=200)
    habitant = models.ForeignKey(Profil , on_delete=models.CASCADE)
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    etat = models.BooleanField(default=False)
    vue = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image_alerte',blank=True)

class evenement(models.Model):
    Titre = models.CharField(max_length=200)
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    type_evenement = models.CharField(max_length=2)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='evenement',blank=True)