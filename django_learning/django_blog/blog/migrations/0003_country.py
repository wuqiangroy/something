# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 15:38
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170709_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', blog.models.ListField()),
            ],
        ),
    ]