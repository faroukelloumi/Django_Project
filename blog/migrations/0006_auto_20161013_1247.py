# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='prenom',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='adresse',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nom',
            field=models.CharField(max_length=40),
        ),
    ]
