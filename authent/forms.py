#-*- coding: utf-8 -*-

from django import forms
from models import Profile
from django.contrib.auth.models import User



class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class UserForm(forms.Form):

    last_name = forms.CharField(label="Nom", max_length=30)
    first_name = forms.CharField(label="Prenom", max_length=30)
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    #avatar = forms.ImageField(label='Avatar', required=False)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        username = cleaned_data.get('user')
        email = cleaned_data.get('email')
        for user in User.objects.all():
            if user.username == self.cleaned_data.get('username'):
                raise forms.ValidationError("Ce pseudonyme est déjà utilisé !")
            elif user.email == self.cleaned_data.get('email'):
                raise forms.ValidationError("Cet email est déjà utilisé !")

        return cleaned_data  # Ne pas oublier de renvoyer le contenu du champ traité

class ProfileForm(forms.Form):
    avatar = forms.ImageField(label='Avatar')