# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playercard',
            name='flavour',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'sweet', b'sweet'), (b'spicy', b'spicy'), (b'salty', b'salty'), (b'tasty', b'tasty')]),
        ),
        migrations.AlterField(
            model_name='playercard',
            name='order',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'first', b'first'), (b'second', b'second'), (b'desert', b'desert'), (b'drink', b'drink')]),
        ),
    ]
