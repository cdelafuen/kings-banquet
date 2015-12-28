# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20151228_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playercard',
            name='order',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'first', b'first'), (b'second', b'second'), (b'dessert', b'dessert'), (b'drink', b'drink')]),
        ),
    ]
