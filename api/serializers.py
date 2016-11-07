from rest_framework import serializers
from blog.models import *

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        exculde = ()


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('nom', 'prenom', 'adresse')

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('nom', )