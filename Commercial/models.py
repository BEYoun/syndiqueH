from django.db import models

# Create your models here.
class accSyndic(models.Model):
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)