# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('citizen', '0001_initial'),
        ('police', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='police.Police'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='citizen.Citizen'),
        ),
    ]
