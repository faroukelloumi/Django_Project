#-*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import *


class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('id', 'titre', 'auteur', 'date', 'apercu_contenu', 'categorie')
   list_filter    = ('auteur','categorie',)
   date_hierarchy = 'date'
   ordering       = ('date', 'id' )
   search_fields  = ('titre', 'contenu')
   fieldsets = (
       # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
           'classes': ['collapse', ],
           'fields': ('titre', 'auteur', 'categorie')
       }),
       # Fieldset 2 : contenu de l'article
       ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu',)
       }),
   )

   def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension.
        """
        text = article.contenu[0:40].encode('UTF-8')
        if len(article.contenu) > 40:
            return '%s…' % text
        else:
            return text

        apercu_contenu.short_description = 'Aperçu du contenu'.encode('UTF-8')

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact)
