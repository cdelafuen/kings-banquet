# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerCard',
            fields=[
                ('card_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='card.Card')),
                ('name', models.CharField(max_length=100)),
                ('cal', models.PositiveSmallIntegerField()),
                ('order', models.CharField(max_length=45, null=True, choices=[(b'first', b'first'), (b'second', b'second'), (b'desert', b'desert'), (b'drink', b'drink')])),
                ('flavour', models.CharField(max_length=45, null=True, choices=[(b'sweet', b'sweet'), (b'spicy', b'spicy'), (b'salty', b'salty'), (b'tasty', b'tasty')])),
            ],
            bases=('card.card',),
        ),
    ]
