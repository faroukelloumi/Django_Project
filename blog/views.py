#-*- coding: utf-8 -*-


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from datetime import datetime
from blog.models import *
from blog.forms import *
from django.views.generic import TemplateView, ListView, DetailView, FormView, RedirectView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.files import File
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, EmptyPage



class ListArticle(ListView):
    """ Afficher tous les articles de notre blog """
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/list_article.html'
    paginate_by = 5


class LireArticle(DetailView):
    """ Afficher un article complet """
    model = Article
    context_object_name = 'article'
    template_name = 'blog/lire.html'

    def get_object(self):
        article = super(LireArticle, self).get_object()
        article.nb_vues += 1
        article.save()
        return article


def Home(request):
    user = request.user
    return render(request, 'blog/accueil.html')


def list_articles(request, month, year):
    text = "Vous avez demandé la liste d'articles de ", year, month
    return HttpResponse(text)

def redirection(request):
    return redirect('blog/home')

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

@cache_page(60 * 15)
def addition(request, n1, n2):
    total = int(n1) + int(n2)
    return  render(request, 'blog/addition.html', locals())

@cache_page(60 * 15)
def condition(request, sexe):
    return render(request, 'blog/condition.html', locals())

@cache_page(60 * 15)
def boucle(request, choix):
    bouc = []
    if choix == "couleur":
        bouc = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
    else:
        bouc = ["Homme", "Femme"]
    return render(request, 'blog/boucle.html', locals())

class CategorieCreate(CreateView):
    template_name = 'blog/add_categorie.html'
    model = Categorie
    success_url = '/blog/add_categorie'
    fields = ('nom',)

    def get(self, request, *args, **kwargs):
        form = CategorieForm()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            print "categrie saved"
            messages.success(request, 'Votre nouvelle categorie a été ajoutée !')

        return render(request, self.template_name, locals())



def add_article(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre article a été ajouté !')
    else:
        form = ArticleForm()

    return render(request, 'blog/add_article.html', locals())


class ListContact(ListView):
    template_name = 'blog/view_contact.html'
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 3


def add_contact(request):

    sauvegarde = False
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            sauvegarde = True
    else:
        form = ContactForm()


    return render(request, 'blog/add_contact.html', locals())








