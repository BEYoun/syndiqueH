from django.db import models
from Accounts.models import Batiment
from django.contrib.auth.models import User
class accHabitant(models.Model):
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
class documentBatiment(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='documentBatiment/')
    batiment = models.ForeignKey(Batiment , on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
class todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
class Email_envoi(models.Model):
    To = models.ForeignKey(User , on_delete=models.CASCADE)
    cc = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)

class Email_recep(models.Model):
    emails = models.ForeignKey(Email_envoi , on_delete=models.CASCADE)
    from_email=models.OneToOneField(User , on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)