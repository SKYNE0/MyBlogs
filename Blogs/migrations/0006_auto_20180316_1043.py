# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0005_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='Blogs.Tag', verbose_name='标签'),
        ),
    ]