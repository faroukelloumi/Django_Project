#-*- coding: utf-8 -*-


from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files import File
from authent.forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)




def connexion(request):

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return HttpResponseRedirect('/blog/home')
            else: # sinon une erreur sera affichée
                messages.error(request, 'Utilisateur ou mot de passe inconnu')
    else:
        form = ConnexionForm()

    return render(request, 'authent/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect('connexion')

def enregistrement(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            last_name = form.cleaned_data["last_name"]
            first_name = form.cleaned_data["first_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)

            return HttpResponseRedirect('/blog/home')

    else:
        form = UserForm()

    return render(request, 'authent/add_user.html', locals())

def add_avatar(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.avatar=form.cleaned_data['avatar']
            messages.success(request, 'Votre avatar a été sauvegardé !')
            profile.save()
    else:
        form = ProfileForm()

    return render(request, 'authent/add_avatar.html', locals())

# Create your views here.
