from django.conf.urls import url
from . import views





urlpatterns = [
    url(r'^test_i18n$', views.test_i18n),
               ]