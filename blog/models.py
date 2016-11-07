from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name='Date de parution')
    nb_vues = models.IntegerField(default=0)
    categorie = models.ForeignKey('Categorie')

    def est_recent(self):
        from datetime import datetime
        return (datetime.now() - self.date).days < 30 and self.date < datetime.now()

    def __str__(self):
        return self.titre


class Categorie(models.Model):
    nom = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nom



class Contact(models.Model):
    prenom = models.CharField(max_length=40)
    nom = models.CharField(max_length=40)
    adresse = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.nom


