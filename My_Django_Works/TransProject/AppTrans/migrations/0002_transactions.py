# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTrans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateoftrans', models.DateField()),
                ('description', models.TextField()),
                ('transcategory', models.TextField()),
                ('amount', models.TextField()),
            ],
        ),
    ]
