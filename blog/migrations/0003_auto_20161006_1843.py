# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161006_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(default=1, to='blog.Categorie'),
            preserve_default=False,
        ),
    ]
