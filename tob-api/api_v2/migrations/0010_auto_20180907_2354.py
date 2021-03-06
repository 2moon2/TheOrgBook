# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-07 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0009_auto_20180907_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='cardinality_hash',
            field=models.TextField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='credentialtype',
            name='logo_b64',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='issuer',
            name='logo_b64',
            field=models.TextField(null=True),
        ),
    ]
