from django.conf.urls import url
from . import views





urlpatterns = [
    url(r'^home$', views.Home, name='home'),
    url(r'^list_article/$', views.ListArticle.as_view(), name='list_article'),
    url(r'^article/(?P<pk>\d+)$', views.LireArticle.as_view(), name='article'),
    url(r'^articles/(\d{2})(\d{4})$', views.list_articles),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<n1>\d+)/(?P<n2>\d+)/$', views.addition),
    url(r'^condition/(?P<sexe>\w*)$', views.condition),
    url(r'^boucle/([A-Za-z]+)$', views.boucle),
    url(r'^add_contact$', views.add_contact),
    url(r'^add_article$', views.add_article, name='add_article'),
    url(r'^add_categorie$', views.CategorieCreate.as_view(), name='add_categorie'),
    url(r'^view_contact$', views.ListContact.as_view(), name='view_contact'),

                       ]