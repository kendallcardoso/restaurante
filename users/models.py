from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    fotodeperfil = models.ImageField(upload_to="imgPerfil/",blank=True,null=True)
    primeirologin =models.BooleanField(default=True)
    telefone = models.CharField(max_length=15 , blank=True,null=True)
    
