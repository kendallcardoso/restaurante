from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200,null=True,blank=True)
    categoria = models.CharField(max_length=200,null=True,blank=True)
    subcategoria = models.CharField(max_length=200,null=True,blank=True)
    preco = models.DecimalField(max_digits=15,decimal_places=2)
    descricao = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to="produtos/",blank=True,null=True)
    dataCadastro = models.DateField(auto_now_add=True)
    responsavel = models.CharField(max_length=100 ,blank=True,null=True)
    destaque = models.BooleanField(default=False , blank=True,null=True)