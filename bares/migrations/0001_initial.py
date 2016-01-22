# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('num_visitas', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tapa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('votos', models.IntegerField(default=0)),
                ('bar', models.ForeignKey(to='bares.Bar')),
            ],
        ),
    ]
