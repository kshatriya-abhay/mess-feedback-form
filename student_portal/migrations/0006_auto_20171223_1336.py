# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-23 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0005_auto_20171223_1323'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='messfeedback',
            unique_together=set([('username', 'year'), ('username', 'month')]),
        ),
    ]
