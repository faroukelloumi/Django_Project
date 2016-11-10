#-*- coding: utf-8 -*-

from django import forms
from models import Article, Categorie, Contact
from django.contrib.auth.models import User
from django.contrib import messages

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude =()

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        prenom = cleaned_data.get('prenom')
        nom = cleaned_data.get('nom')
        for con in Contact.objects.filter(nom=nom, prenom=prenom):
            if con.prenom == self.cleaned_data.get('prenom') and con.nom == self.cleaned_data.get('nom'):
                print 'mawjoud'
                raise forms.ValidationError("Ce contact existe déjà !")

        return cleaned_data  # Ne pas oublier de renvoyer le contenu du champ traité


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude =('date', 'nb_vues' )

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        titre = cleaned_data.get('titre')
        auteur = cleaned_data.get('auteur')
        for artic in Article.objects.filter(titre=titre, auteur=auteur):
            if artic.titre == self.cleaned_data.get('titre') and artic.auteur == self.cleaned_data.get('auteur'):
                raise forms.ValidationError("Cet article existe déjà !")

        return cleaned_data  # Ne pas oublier de renvoyer le contenu du champ traité

class CategorieForm(forms.ModelForm):

    class Meta:
        model = Categorie
        fields =('nom', )


    def is_valid(self):
        valid = super(CategorieForm, self).is_valid()
        if not valid:
            return False
        nom = self.cleaned_data.get('nom')
        print Categorie.objects.filter(nom=nom)
        try:
            Categorie.objects.get(nom=nom)
            return False
        except :
            return True




