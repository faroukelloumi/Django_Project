from django.test import TestCase

from django.test import TestCase
from datetime import datetime, timedelta
from models import Article


class ArticleTests(TestCase):
    def test_est_recent_avec_futur_article(self):

        futur_article = Article(date=datetime.now() + timedelta(days=20))
        # Il n'y a pas besoin de remplir tous les champs, ni de sauvegarder
        self.assertEqual(futur_article.est_recent(), False)
