from rest_framework import viewsets

from .serializers import *


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CategorieViewSet(viewsets.ModelViewSet):

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer