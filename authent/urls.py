from django.conf.urls import url
from . import views





urlpatterns = [
    url(r'^add_avatar$', views.add_avatar, name='add_avatar'),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
    url(r'^enregistrement$', views.enregistrement, name='enregistrement'),
                       ]