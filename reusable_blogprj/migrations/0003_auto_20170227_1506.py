# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable_blogprj', '0002_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
    ]