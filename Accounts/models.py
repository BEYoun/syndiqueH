from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Batiment(models.Model):
    nom = models.CharField(max_length=100)
    nbrApp = models.IntegerField()
    nbrResidant = models.IntegerField()
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{0}".format(self.nom)

class Appartement(models.Model):
    nom = models.CharField(max_length=100)
    etage = models.IntegerField()
    nombreHabitant = models.IntegerField()
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
class Profil(models.Model):
    MANAGER = 'MA'
    COMMERCIAL = 'CM'
    VALIDATEUR = 'VA'
    HABITANTP = 'HP'
    HABITANTL = 'HL'
    SYNDIQUE = 'SY'
    NOUVEAUH = 'NV'
    Role = [
        (MANAGER, 'Manager'),
        (COMMERCIAL, 'Commercial'),
        (VALIDATEUR, 'Validateur'),
        (HABITANTP, 'Habitant Permanent'),
        (HABITANTL, 'Habitant Locataire'),
        (SYNDIQUE, 'Syndique'),
        (NOUVEAUH, 'Nouveau Habitant'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    role = models.CharField(max_length=2,choices=Role,default=HABITANTP)
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE,default=1)
    appartement = models.ForeignKey(Appartement , on_delete=models.CASCADE,default=2)
    image = models.ImageField(upload_to='profile_image',blank=True)
    def __str__(self):
        return "Profil de {0}".format(self.user.username)
    
class newAcc(models.Model):
    MANAGER = 'MA'
    COMMERCIAL = 'CM'
    VALIDATEUR = 'VA'
    HABITANTP = 'HP'
    HABITANTL = 'HL'
    SYNDIQUE = 'SY'
    NOUVEAUH = 'NV'
    Role = [
        (MANAGER, 'Manager'),
        (COMMERCIAL, 'Commercial'),
        (VALIDATEUR, 'Validateur'),
        (HABITANTP, 'Habitant Permanent'),
        (HABITANTL, 'Habitant Locataire'),
        (SYNDIQUE, 'Syndique'),
        (NOUVEAUH, 'Nouveau Habitant'),
    ]
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    numero = models.CharField(max_length=13)
    typeClient = models.CharField(max_length=2,choices=Role)
    ville = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    quartier = models.CharField(max_length=10)
    etat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



@receiver(post_save, sender=User)
def update_user_profil(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)
    instance.profil.save()