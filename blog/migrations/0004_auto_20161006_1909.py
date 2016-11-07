# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161006_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prix', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vendeur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
                ('produits', models.ManyToManyField(to='blog.Produit', through='blog.Offre')),
            ],
        ),
        migrations.AddField(
            model_name='offre',
            name='produit',
            field=models.ForeignKey(to='blog.Produit'),
        ),
        migrations.AddField(
            model_name='offre',
            name='vendeur',
            field=models.ForeignKey(to='blog.Vendeur'),
        ),
    ]
